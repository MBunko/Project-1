# Videogame review site

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



## Software design


### ERD  
  
ERD built with Lucid.app  
  
![ERD][Initial ERD]  
  
![ERD2][ERD2]

### CI pipeline



## Project planning

### Trello board  
  
Below is the initial Trello board from the start of the project:  
  
![TB1][TB1]  
  
Here is the link to my Trello board: https://trello.com/b/EcXuFyAV/sfia-project-1  
Below is my current Trello board:
  
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

###Week 1-3:
A list of risks identified at the star of the project with limited knowledge 
|Risk Description|Likelihood of the risk occurring|Impact if the risk occurs|Severity rating based on impact and likelihood|Risk owner|Mitigating action(actions to mitigate risk or reduce likelihood)|Contingent action.  (Actions to be taken if the risk happens)|  
|---|---|---|---|---|---|---|  
|Log in overwrite|medium|high|high|Me|Create check for existing email or create unique auto generated ID|Create listing on login page not to create a second account with same username or email address|  
|Server failure|low|high|medium|Server provider|Possibly create backup|None|  
|Traffic overload|low|low|low|Me + server provider|Likely none- could use service analytics and buy space accordingly|Post on site times likely to be down|  
|Bugs in coding|high|high|high|Me|Finish task ahead of schedule to gain time to debug|Debug program|  
|Lack of knowledge|low|high|medium|Me + trainers|Ask questions in lectures on concerns and revise notes regularly|Ask for clarification on lacking knowledge during project and do personal research|  
|Password hack|low|Very high|high|Me|Could try to hash passwords or not tie sensitive info to account|Immediately report hack|

### Final assessment

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
