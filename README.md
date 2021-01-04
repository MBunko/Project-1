# Metagamer- A videogame review site

### Contents

1. [Brief](#Brief) 
2. [Software design](#Software-design)
 2.1. [ERD](#ERD)
 2.2. [CI pipeline](#CI-pipeline)
3. [Project planning](#Project-planning)
 3.1. [Trello board](#Trello-board)
 3.2. [Expanded user stories](#Expanded-user-stories)
4. [Risk assessment](#Risk-assessment)
5. [Testing](#Testing)
 5.1. [Unit testing and integration testing](#Unit-testing-and-integration-testing)
 5.2. [Testing coverage](#Testing-coverage)
6. [Front end](#Front-end)
7. [Evaluation](#Evaluation)
 7.1. [Issues](#Issues)
 7.2. [Possible improvements](#Possible-improvements)
8. [Appendix](#Appendix)
 8.1. [Licensing](#Licensing)
 8.2. [Contributors and Acknowledgement](#Contributors-and-Acknowledgement)







## Brief  
The general objective of this project according the project specification is "to create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training" where CRUD refers to an application with Create. Read, Update and delete functionality.  
Exact requirements for the project beyond CRUD functionality include use of: 

* A Kanban Board.
* Design documentation and a readme with all relevant content.
* A cloud hosted database with 2 tables and a one to many relationship.
* Python programming.
* Unit Testing with Pytest.
* Integration Testing with Selenium.
* Flask HTML front end design.
* Git for version control.
* Jenkins as a CI server.
* A Cloud server.
* ERD and CI pipeline diagrams.
* A risk assessment.

For my project I will be creating a basic game review application that allows users to add games and reviews to the application, view all the games and their reviews as well as update and delete their own reviews.


## Software design

Throughout the project various software has been used in the creation, testing, and implementation of the application. Some of these software will be covered in more depth later in the readme but this section will show a few diagrams to generally show and explain the software implemented.  

To start the application was created using Flask which is a python based micro-framework alongside HTML for the pages. As a micro-framework Flask has low built in functionality but has many possible extensions making it very flexible and therefore ideal for a simple project such as this. All installed extensions can be found in the requirements.txt file within this repo.  

### ERD  

An ERD is an entity-relationship diagram and is used to show the relationships between 2 or more tables within a database. For this project my database tables were created with the create.py and models.py files that can be found within this repository and were created in a private MySQL server on Google cloud platform (GCP) to keep the databases secure and directly accessible by me only. MySql has been used because the application has been made using Flask which has extensions that make it compatible with MySQL meaning the database tables can be easily created, viewed, modified and deleted from the front end all through functionality created by Flask.

Below is my initial ERD created at the very start of the project before I fully understood the tools I would be using to create the application:
  
  
ERD built with Lucid.app  
  
![ERD][Initial ERD]  
 
As you can see the initial diagram contains a user login table tied to the reviews, however this was not a part of the project specification and added unnecessary complication and potential issues to the project so as I started working on the project the design eventually evolved into the below diagram which matches the actual tables now stored in my MySQL server:  
 
![ERD2][ERD2]

As you can see my final design consists of two tables with a one to many relationship (one game to many reviews). Each game entry in the database consists of a game title as it’s primary key both to ensure that titles are unique and to make the title the foreign key for the reviews to make referencing somewhat easier. The other fields for this table are just generic information required for any game and have a 30 character limit with the exception of the description which can allow for 300 characters.  

If you look at the changes between the initial review table and the final one you will notice that the login has been replaced with a reviewer name (which is a nullable field) and a review password so that the password can be made for the review so that it can be updated and deleted only by someone who knows the password to keep a level of security without need for login functionality. Another change is the inclusion of review date time which automatically inputs the date and time the review is initially posted to provide more information to those reading the review. The final change is the inclusion of a review title to allow users to further customise and distinguish their reviews. The review ID is an auto increment integer to make for an ideal primary key allowing for any of the fields entered by the users to match up with another review without causing issues. You can also see that the Game title from the games tables is the foreign key that connects the review to the game.


### CI pipeline

Below is a continuous integration (CI) pipeline diagram showing how all the software involved in the project connects. The heart of CI pipeline is the CI server which allows for continuous and automatic integration of new code. For this project I am using Jenkins because it is a free CI server that can easily be installed and managed on a simple linux VM meaning it can be cheaply run on it's own VM server with a unique private IP address. I will be using Jenkins to automatically build and test the application every time a change is made to the Github repository as will be explained beneath the diagram.  

![CI][CI]


The top line depicts the development side with visual studio code (VSC) being the IDE I used and python being the programming language the app was built in as Flask is python based. Whenever a part of the project is completed it is then pushed to Github which is my version control system (VCS) serving both as a repo for my project and as a record of all changes and versions of the files and branches throughout the project allowing for easy debugging. Github was chosen because it is a free open source VCS that allows my project and changes to be viewed publicly. Finally we have my Trello board used for tracking the project that is used in tandem with the Github repo to determine what work needs to be done for Github and what tasks need to be updated on Trello.

The second line as well as the HTML report is the devops side of the pipeline. A webhook is used to pull a copy of the Github repo to the Jenkins server automatically every time it is updated, Jenkins then creates a build of the project and uses Pytest to test that all decided tests still pass with all the new changes and pytest cov builds a coverage report to show what percentage of the related files are covered. If the build fails (meaning Pytest has failed to pass all tests or the app cannot be run) or if coverage is no longer within an acceptable range then the error is shown and debugging is done in VSC. Regardless this data is saved as an HTML report which is the artefact for the build. More information on this part is provided in the testing section of the readme. 

Finally we have the live testing section of the pipeline. After the artefact is checked and cleared the app is tested in google cloud platform to make sure it works in the environment it will be running in  and if the human QA tester (in this first sprint me) has no issues with it, it will be pushed to the live environment also on google cloud platform. The only difference between the live environment and the test environment is that debug mode is on in the test environment so that I can see an error report for any issues caused. If there were any issues then these are again debugged in VSC and the cycle starts over again.

## Project planning

This project was planned and tracked using a Trello board because it is a free, simple, and easy to use Kanban board that can be made public to view.

### Trello board  
  
Below is the initial Trello board from the start of the project:  
  
![TB1][TB1]  

The above initial board basically lists the requirements on the specification as the To do must section. Below you will see the evolution of cases, tasks and task sections between the beginning of the project and now as the requirements have been exapnded into a multitude of tasks and the range of user stories have been increased.
  
Here is the link to my Trello board: https://trello.com/b/EcXuFyAV/sfia-project-1  
Below is my current Trello board:

![TB2][TB2]

The sections for the Trello board above start with a list of user stories split into what the user and host wants available as a result of the project. The rest of the board is split into the sections “To Do” which are tasks not yet started, “In progress” which are tasks currently being worked on, “Done” which is finished tasks and “Not Done” which are tasks that were abandoned and not finished. Each section is further split into “Must” which are tasks that have to be completed to keep in line with passing the project, “Should” which are tasks that should be completed in order to make sure the project is at a high standard and receives above average scores and “Could” which are tasks that could help reach maximum marks or would otherwise improve the project beyond the scope of the project.   The Not done section does not specify type as it would be unacceptable to have Must tasks in the not done section. 

### Expanded user stories  
  
Here is a table of user stories expanded to give full meaning to them so that if there were any issues implementing the tasks the expanded user stories could be checked to see if there were any other paths to reaching the desired destination:

|As a…|I want to…|	So that I can…|Priority|
|---|---|---|---|
|User|See new reviews|Be informed on products|Must
|User|Search for specific titles|Know if a product I’m interested in is worth my time/money|Should
|User|Have an uncluttered and intuitive website|Can easily navigate the site and find what looking for|Must
|User|Add reviews|Create a new review  for a game I finished|Must
|User|Update reviews|Make changes to my review in case of mistakes or change in opinion|Must
|User|Delete reviews|Remove a review  I no longer agree with or regret|Must
|User|See aggregate reviews|See general consensus on games|Should
|Host|Have an uncluttered back end|Run it cheaply and debug issues more easily|Should
|Host|Have a secure database off site|Make sure no one can reformat my database or see peoples passwords|Must
|Host|Have automated testing, running and integration|Have a site that’s constantly up and to reduce my repetitive workload|	Must




## Risk assessment 

### Week 1-3:
Below is a list of risks identified at the star of the project with limited knowledge of the tools used and project scope.
|Risk Description|Likelihood of the risk occurring|Impact if the risk occurs|Severity rating based on impact and likelihood|Risk owner|Mitigating action(actions to mitigate risk or reduce likelihood)|Contingent action.  (Actions to be taken if the risk happens)|  
|---|---|---|---|---|---|---|  
|Log in overwrite|medium|high|high|Me|Create check for existing email or create unique auto generated ID|Create listing on login page not to create a second account with same username or email address|  
|Server failure|low|high|medium|Server provider|Possibly create backup|None|  
|Traffic overload|low|low|low|Me + server provider|Likely none- could use service analytics and buy space accordingly|Post on site times likely to be down|  
|Bugs in coding|high|high|high|Me|Finish task ahead of schedule to gain time to debug|Debug program|  
|Lack of knowledge|low|high|medium|Me + trainers|Ask questions in lectures on concerns and revise notes regularly|Ask for clarification on lacking knowledge during project and do personal research|  
|Password hack|low|Very high|high|Me|Could try to hash passwords or not tie sensitive info to account|Immediately report hack|

### Final risk assessment
Below is my risk assessment from the end of the project with a better understanding of the tools and problems to be faced. There aren't many different risks from above however the mitigating actions and contigent actions taken and to be taken have changed through the development. 
|Risk Description|Likelihood of the risk occurring|Impact if the risk occurs|Severity rating based on impact and likelihood|Risk owner|Mitigating action(actions to mitigate risk or reduce likelihood)|Contingent action.  (Actions to be taken if the risk happens)|  
|---|---|---|---|---|---|---|  
|Log in overwrite|medium|high|high|Me|Removed login functionality|Can no longer happen|
|Incorrect data entry|Very high|low|medium|Me + User|Set up validators and error messages to prevent invalid data from going into the database and to let users know their mistakes| Find the mistake and add appropriate further validators.|
|PC failure (data loss)|low|high|medium|Me|Copy of data on GCP and Github and regularly pushed|Download data back to machine| 
|Server failure (VM)|low|high|medium|Server provider|Have local copy and copy on 2 seperate online services|Upload local copy when server back up|  
|Server failure (MySQL)|low|high|medium|Server provider| Have second copy of database that's regularly updated| Consider having application write data to 2 spearate databases from the start|
|Traffic overload|low|low|low|Me + server provider|Likely none- could use service analytics and buy space accordingly|Post on site times likely to be down|  
|Bugs in coding|high|high|high|Me|Finish task ahead of schedule to gain time to debug|Debug program|  
|Lack of knowledge|low|high|medium|Me + trainers|Ask questions in lectures on concerns and revise notes regularly|Ask for clarification on lacking knowledge during project and do personal research|  
|Password hack|low|Very high|high|Me+ user (password strength)|Passwords tied to review and not account so no email or account is compromised|None (would not know as no account hacked)|
|Avoiding password requirements through URL manipulation|High|High|High|Me|URL itself for deleting and editing reviews now requires password|Create user login if way around discovered|

## Testing

The testing software used for this project is Pytest which is a python testing framework that clearly tests functionality and much like Flask is fairly extensible as there are several installable modules to go with it. The only ones needed for this project is Pytest-cov which is a module designed to show how much of the code in files or folders is actually tested by the tests and selenium which allows for integration testing which will be discussed below. There is also a pytest-coverage module however pytest-cov can be used to generate HTML reports which can be archived and easily read through Jenkins which will be discussed in the Jenkins section of the readme which is why it was chosen.


### Unit testing and integration testing

The fundamental purpose of unit testing in this project was to test CRUD (create, read, update, delete) functionality, making sure that each function/URL performs whichever of those tasks it was designed to. In the below front end section I will go into more detail about each page but the first set of unit tests simply checked that each page could be visited without returning an error. This test has been applied to every single page as they are all designed to be used in some capacity. The next test was just to see that when the homepage was visited it could be read showing that the page would display as intended from the start. The reason this was the only page tested in this way is because all other pages are tested in other ways which include additions and changes performed within them being read on those pages or others. 

The next set of tests were add tests. These were designed to see if going to the page to add games to the database or the page to add reviews would then on redirect make the additions readable on the page. This checks that the add pages are working as designed and that read functionality was working correctly on the pages that would display their additions. I also had separate tests in this category to check if upon adding an invalid Game or review (for the game giving it a release date of “today” when the form only accepts them in the form of yyyy-mm-dd and for the review giving it a score of 15 when the form only accepts numbers 1-10) that it would redirect to the error page and be able to read the error message. 

Next was for updating a review. The review to be updated was created as part of the test set up so that it would be available to read and change. First I tested that upon entering the correct password to match the review you would be redirected to the page that would allow you to update the review and also that entering the incorrect password would not. I then tested that altering the review would make the new review readable on the review page (ensuring it was reading specifically altered parts of the review) and that entering invalid information (again using a rating over 10 for the test) that it would redirect to an error page.

Finally I tested delete functionality by testing that upon entering the password correctly while attempting to delete that the review would no longer be visible on the reviews page.

For integration testing, firstly both the above unit testing and below selenium testing were done on a separate database on the same MySQL server that the application uses therefore testing integration between Flask and the MySQL database as the tests will fail to read any games or reviews if it cannot connect to the server they are being stored on.

Secondly I used selenium testing which tests functionality by having the program actually going to the webpage, entering information directly to the page and clicking the buttons to navigate rather than forcing redirects. This tests that functionality applies to the web application and not just the URL functions. For this test I first tested that the server was properly running to make sure the test would be also able to properly run. Then I simply tested that the adding of a game unit test could be recreated with the test using the web application to perform it as if it were a user. I only did this for one unit test as if one test works correctly in a live environment the rest should do the same. It should also be noted that I was personally testing the functionality in the same environment directly after all tests passed as was shown in the CI pipeline so it would be directly noticed if there was any inconsistency.

![Pytest][Pytest]

As you can see at the bottom every single test for both integration and unit testing passed successfully showing that the program works as intended and passes CRUD functionality. This means that every single page can be visited without error. The home page can be viewed and read. Games and reviews can be added to the database and read in their respective pages and pre-existing reviews can be updated with the same result. Incorrect entry of data into a form for creating or updating entries to the database will redirect to the error page and the error message can be read. Correct entry of the password to update a review will redirect to the page where user can change the details of their reviews and for deletion correct entry will return to the games page where the review can no longer be read. The fact that the tests relating to the database pass also means that connection to the SQL database is also successful. For selenium testing this means the application runs on startup and that the unit tests for going from the home page to the add page and successfully adding an entry to the database and reading it on the web application works identically when using the web browser and manually performing the tasks to when done through the functions. 

### Testing coverage

For the coverage test I used Pytest –-cov=application to check the testing coverage for the models.py, routes.py and __init__.py file. The __init__.py file is the set up file for functionality so it needs to be fully used by the test to show the test is set up correctly. The models.py file contains all the tables for the database as well as the forms used to make changes and reference the tables so the tests need to use this fully. Finally the routes.py file contains all the webpages and their functionality so it is important that we check how much of it is covered by the tests. A minimum requirement would be 75% coverage here as it would show the tests are checking the majority of functionality though 100% would be ideal.

![Cov][Cov]

As you can see my tests cover 100% of all files meaning that the full breadth of the application has been tested making the tests a success.

## Front end

This section will cover the front end of my project. It is very basic and aesthetic design has not been a factor at this stage in the project beyond being easily navigated and understood and only CRUD functionality has been prioritised.

As you can see below, every single page with the exception of /delete which performs a delete function and redirects to the home page automatically has two buttons at the top that allow for navigation to the home page and to the page that allows users to add a new game to the database.

![F1][F1]

Above is the home page. It contains an alphabetical list of all games in the database listed under the letter they begin with. At the bottom of the page is a “.” category that lists all games that begin with a number or special character. As you can see you can click view game to be taken to the games page.

![F2][F2]

This page allows the user to add a new game to the database. Release date is in the form of YYYY-MM-DD and the game will not be added if it is not in this format.

![F3][F3]

This is the game page. It displays the data for a game selected on the home page. It also has a button that allows a user to create a new review as well as showing an aggregated review score and a list of reviews. You can see here that with no reviews there is a special message to let the users know there are no reviews and therefore no score.

![F4][F4]

This is the review page that allows a user to create a new entry for the game whose page they were previously on.

![F5][F5]

This is a custom error page. This is for adding a review but there is also one for adding a new game and for updating a review. It tells the user that they made an error at the top of the page next to the navigation menu and also displays a message by the invalid field to let them know what their mistake is.

![F7][F7]

Here you can see the game page complete with a review and the aggregated score. You can also see that for each review there is an edit and delete button.

![F8][F8]

Upon clicking the update button the user is redirected to this password screen to enter the password tied to the review. If entered incorrectly the page will simply reload.

![F9][F9]

Upon successful password entry the user is redirected to the update page. The fields are identical to the add a review page however it does display the title of the original review for reference.

![F10][F10]

The final page is the delete page. Just like for updating pressing the delete review button redirects to a password screen. Upon entering a successful password the user is redirected back to the games page with the review deleted.


## Evaluation

### Issues

The main issue with the project is the use of Google cloud platform to host my servers. It was chosen because it provides a free trial which is ideal during training, however upon stopping a VM to preserve trial credit the IP address is not saved. This means that automated integration is not fully automated as on stopping and starting the VMs requires giving the new IP access to Githubs webhook and to the MySQL server.

Further the MySQL server can also change IP. Because the service that runs the app is a daemon (background process) it stops functioning when this occurs and is difficult to change since it is within the systemD. This meant that my Jenkins build that runs the app no longer functioned. So while Jenkins does automatically run pytest it does not run the app.   

Finally, to an outsider some of my code may seem somewhat confusing. For example there are 3 routes relating to updating the reviews, update which asks for the password to update, change which allows the user to actually alter the data in the table and edit which asks for the password so that it can redirect to the delete route. Also because update and edit both use the same form they also both use the delete.html for password entry. In future, I will have to think more about people using my work as a reference and label my titles and functions for their benefit instead of mine or otherwise label my code as I write it with help for viewers utilising a #. 

### Possible improvements

Beyond learning how to avoid the above mentioned issue the main ways to improve on this project moving forward would be the inclusion of login functionality for added security and to make the web application aesthetically appealing to compete with modern websites. Additional improvements would be the inclusion of a search bar to help find games and reviews by title or user and a function to write the table entries to two separate databases simultaneously to save the data in case the server goes down. Finally, I could have my selenium testing cover the full range of unit tests for complete testing.

## Appendix

### Licensing 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

This permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

### Contributors and Acknowledgement 

Author: Michael Bunko

Acknowledgement: I would like to thank my trainers for their teaching and support including Harry Volker, Jay Grindrod, Nathan Forester and Peter Rhodes.
I would also like to thank the members of my teams during training for their help and support.




[Initial ERD]: https://lucid.app/publicSegments/view/3a71919e-07eb-4370-8853-af7eafda35bd/image.png
[ERD2]: https://lucid.app/publicSegments/view/8967aca1-e6aa-43ec-b392-f9a77eab4f13/image.png
[TB1]: https://i.imgur.com/7YArl2t.png
[TB2]: https://i.imgur.com/p6DrbA1.png
[CI]: https://i.imgur.com/jxxzQ3z.png
[Pytest]: https://i.imgur.com/YuFRW07.png
[Cov]: https://i.imgur.com/z6Ik9oI.png
[F1]: https://i.imgur.com/p1lZMFo.png
[F2]: https://i.imgur.com/4ULXuZw.png
[F3]: https://i.imgur.com/Z3x7x5l.png
[F4]: https://i.imgur.com/B7yWicl.png
[F5]: https://i.imgur.com/YiHqP0l.png
[F7]: https://i.imgur.com/DRLYVtr.png
[F8]: https://i.imgur.com/Y0dTE1S.png
[F9]:https://i.imgur.com/q2OUveJ.png
[F10]: https://i.imgur.com/JKQeZht.png
