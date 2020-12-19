import unittest
from flask import url_for
from flask_testing import TestCase
from os import getenv

from application import app, db
from application.models import Games, Reviews

class Testbase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
            SECRET_KEY=getenv('SECRET_KEY'),
            DEBUG=True
        )
        return app

    def setUp(self):
        db.create_all()
        test_game=Games(Title="test flask app", Release_date="2020-12-18", Genre="Horror", Age_rating="26", Description="All pain")
        db.session.add(test_game)
        db.session.commit()
        test_review=Reviews(Games_title="test flask app", Review_title="test review table", Reviewer_name="pytest", Review_password="password", Review="I hope I can see this", Rating=10)
        db.session.add(test_review)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(Testbase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_add_get(self):
        response = self.client.get(url_for('add'))
        self.assertEqual(response.status_code, 200)

    def test_game_get(self):
        response = self.client.get(url_for('game', Title="test flask app"), follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_review_get(self):
        response = self.client.get(url_for('review', Title="test flask app"), follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_edit_get(self):
        response = self.client.get(url_for('edit', number=1), follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_update_get(self):
        response = self.client.get(url_for('update', number=1), follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_change_get(self):
        response = self.client.get(url_for('change', number=1, pword="password"), follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete', number=1, pword="password"), follow_redirects=True)
        self.assertEqual(response.status_code,200)

class TestRead(Testbase):
    def test_read_tasks(self):
        response= self.client.get(url_for("home"))
        self.assertIn(b"test flask app", response.data)

class TestCreate(Testbase):
    def test_add_task(self):
        response = self.client.post(url_for("add"),
            data=dict(Title="Create a new game", Release_date="2020-12-18", Genre="Horror", Age_rating="26", Description="All pain"),
            follow_redirects=True
        )
        self.assertIn(b"Create a new game", response.data)
    
#class TestUpdate(Testbase):
 #   def test_update_task(self):
 #       response = self.client.post(url_for("update", id=1),
 #           data=dict(entry_name="Update a task", status="incomplete"),
 #           follow_redirects=True
 #       )
 #       self.assertIn(b"Update a task", response.data)

#class TestDelete(Testbase):
 #   def test_update_task(self):
 #       response = self.client.get(url_for("delete", number=1),
  #          follow_redirects=True
  #      )
 #       self.assertNotIn(b"test flask app", response.data)
    