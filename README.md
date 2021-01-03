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
6. [Software development](#Software-development)
 6.1. [Front end](#Front-end)
 6.2. [CRUD functionality](#CRUD-functionality)
7. [Systems build](#Systems-build)
 7.1. [Jenkins](#Jenkins)
 7.2. [Integration test results](#Integration-test-results)
8. [Evaluation](#Evaluation)
 8.1. [Issues](#Issues)
 8.2. [Possible improvements](#Possible-improvements)
9. [Appendix](#Appendix)
 9.1. [Licensing](#Licensing)
 9.2. [Contributors & Acknowledgment](#Contributors-&-Acknowledgment)







## Brief  
The general objective of this project according the project specification is "to create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training" where CRUD refers to an applcation with Create. Read, Update and delete functionality.  
Exact requirements for the project beyond CRUD functionality include use of: 

* A Kanban Board.
* Desgin documentation and a readme with all relevant content.
* A cloud hosted database with 2 tables and a oneto many relationship.
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

To start the applciation was created using Flask which is a python based micro-framework. As a micro-framework Flask has low built in fucntionality but has many possible extensions making it very flexible and therefore ideal for a simple project such as this. All installed extensions can be found in the requirements.txt file within this repo.  

### ERD  

An ERD is an entry relationship diagram and is used to show the relatinships between 2 or more tables within a database. For this project my database tables were created with the create.py and models.py files that can be found within this repository and were created in a private MySQL server on Google cloud platform (GCP) to keep the databases secure and directly accessible by me only. MySql has been used because the applciation has been made using Flask which has extensions that make it compatable with MySQL meaning the database tables can be easily created, viewed, modified and deleted from the front end all through functionality created by Flask.

Below is my initial ERD created at the very start of the project before I fully understood the tools I would be using to create the application:
  
  
ERD built with Lucid.app  
  
![ERD][Initial ERD]  
 
As you can see the initial diagram contains a user login table tied to the reviews, however this was not a part of the project specification and added unnecesary complication and potential issues to the project so as I started working on the project the design eventually evolved into the below diagram which matches the actual tables now stored in my MySQL server:  
 
![ERD2][ERD2]



### CI pipeline

![CI][CI]

## Project planning

### Trello board  
  
Below is the initial Trello board from the start of the project:  
  
![TB1][TB1]  
  
Here is the link to my Trello board: https://trello.com/b/EcXuFyAV/sfia-project-1  
Below is my current Trello board:

![TB2][TB2]

### Expanded user stories  
  
Here is a table of user stories:

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
A list of risks identified at the star of the project with limited knowledge 
|Risk Description|Likelihood of the risk occurring|Impact if the risk occurs|Severity rating based on impact and likelihood|Risk owner|Mitigating action(actions to mitigate risk or reduce likelihood)|Contingent action.  (Actions to be taken if the risk happens)|  
|---|---|---|---|---|---|---|  
|Log in overwrite|medium|high|high|Me|Create check for existing email or create unique auto generated ID|Create listing on login page not to create a second account with same username or email address|  
|Server failure|low|high|medium|Server provider|Possibly create backup|None|  
|Traffic overload|low|low|low|Me + server provider|Likely none- could use service analytics and buy space accordingly|Post on site times likely to be down|  
|Bugs in coding|high|high|high|Me|Finish task ahead of schedule to gain time to debug|Debug program|  
|Lack of knowledge|low|high|medium|Me + trainers|Ask questions in lectures on concerns and revise notes regularly|Ask for clarification on lacking knowledge during project and do personal research|  
|Password hack|low|Very high|high|Me|Could try to hash passwords or not tie sensitive info to account|Immediately report hack|

### Final risk assessment

|Risk Description|Likelihood of the risk occurring|Impact if the risk occurs|Severity rating based on impact and likelihood|Risk owner|Mitigating action(actions to mitigate risk or reduce likelihood)|Contingent action.  (Actions to be taken if the risk happens)|  
|---|---|---|---|---|---|---|  
|Log in overwrite|medium|high|high|Me|Removed login functionality|Can no longer happen|
|PC failure (data loss)|low|high|medium|Me|Copy of data on GCP and Github and regularly pushed|Download data back to machine| 
|Server failure|low|high|medium|Server provider|Have local copy and copy on 2 seperate online services|Upload local copy when server back up|  
|Traffic overload|low|low|low|Me + server provider|Likely none- could use service analytics and buy space accordingly|Post on site times likely to be down|  
|Bugs in coding|high|high|high|Me|Finish task ahead of schedule to gain time to debug|Debug program|  
|Lack of knowledge|low|high|medium|Me + trainers|Ask questions in lectures on concerns and revise notes regularly|Ask for clarification on lacking knowledge during project and do personal research|  
|Password hack|low|Very high|high|Me+ user (password strength)|Passwords tied to review and not account so no email or account is compromised|None (would not know as no account hacked)|
|Avoiding password requirements through URL manipulation|High|High|High|Me|URL itself for deleting and editing reviews now requires password|Create user login if way around discovered|

## Testing

### Unit testing and integration testing


### Testing coverage


## Software development

### Front end

### CRUD functionality


## Systems build

### Jenkins

### Integration test results


## Appendix

### Licensing 

### Contributors & Acknowledgment






[Initial ERD]: https://lucid.app/publicSegments/view/3a71919e-07eb-4370-8853-af7eafda35bd/image.png
[ERD2]: https://lucid.app/publicSegments/view/8967aca1-e6aa-43ec-b392-f9a77eab4f13/image.png
[TB1]: https://i.imgur.com/7YArl2t.png
[TB2]: https://i.imgur.com/p6DrbA1.png
[CI]: https://i.imgur.com/jxxzQ3z.png
