import unittest
import time
from flask import url_for
from urllib.request import urlopen
from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db
from application.models import Games, Add, Reviews, Review, Delete, Update

class TestBase(LiveServerTestCase):

    def create_app(self):

        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
        app.config['SECRET_KEY'] = getenv("SECRET_KEY")
        return app

    def setUp(self):
        """
        Setup the test driver and create table schema before every test.
        You can populate the table with some test tasks here if you want to
        test read/update/delete functionality.
        """
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/jenkins/.jenkins/workspace/Project-1 pytestchromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.drop_all()
        db.create_all()

    def tearDown(self):
        """
        Stop the driver after every test.
        """
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        """
        Test that the server is running before each test.
        """
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)

class TestGameCreation(TestBase):
    def test_game_creation(self):
        """
        Test that a user can navigate to the Create Task page,
        enter the description for the task and check to see if
        it redirects to the home page
        """

        # Navigate to the Create Task page
        self.driver.find_element_by_xpath('/html/body/a[2]').click()
        time.sleep(1)

        # Input the task description into the form field
        self.driver.find_element_by_xpath('//*[@id="Title"]').send_keys('Integration test')
        self.driver.find_element_by_xpath('//*[@id="Release_date"]').send_keys('2020-12-08')
        self.driver.find_element_by_xpath('//*[@id="Genre"]').send_keys('Integration')
        self.driver.find_element_by_xpath('//*[@id="Age_rating"]').send_keys('It')
        self.driver.find_element_by_xpath('//*[@id="Description"]').send_keys('Integration test')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        # Assert that browser redirects to home page
        assert url_for('home') in self.driver.current_url
        assert Games.query.filter_by(Title="Integration test").first().Release_date=="2020-12-08"

if __name__ == '__main__':
    unittest.main(port=5000)
