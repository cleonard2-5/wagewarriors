# Making a fork

1. Go to github, make a fork (This will  allow you to make changes to your code locally incase things go wrong) <br/>
2. run this in your terminal `git clone https://github.com/itsZling/wagewarriors.git` <br/>
3. then change your diretory to the folder (ex. cd wagewarriors) <br/>
4. now run `git remote rename origin <your name>` in your terminal <br/>
5. And finally go back to your fork on Github, copy the link, and run `git remote add origin <your link>` <br/>
<hr/>
This will let you have your own fork, that allows you to make pull requests to main

# Basic GitHub commands

- `git pull` (updates your local code to match main)  **!MAKE SURE YOU ARE UP TO DATE BEFORE WORKING!** <br/>
- `git add .` (adds all new files for staging) **!DO THIS BEFORE COMMITING!** <br/>
- `git commit -am "<message of what changes you made since last commit>"` (commits all changes made with the message you put in the quotes) <br/>
-  `git push origin` (pushes all changes to Github from local) <br/>
<hr>
when you want everyone to use your changes:
go back to your Github fork and click contribute --> pull request

# django commands
### (use `python3` for mac)
-  `python manage.py startapp <appname>` (to create an app) <br/>
-  `python manage.py runserver` (to run website) <br/>
-  `python manage.py createsuperuser` (to make an admin account) <br/>
-  `python manage.py makemigrations` + `python manage.py migrate` (to add migrations made in admin) <br/>
<hr>

# Tasks
- valid pasword and email check. <br/>
- unique username, but allow duplicate companies. <br/>
- <s>add a edit button to profile to allow users to change information. </s><br/>
- send proper errors when signup/login fails. <br/>
- <s>profile has username in the url.  </s><br/>
- Add custom colors to allow for a purple overall theme. <br/>

to access a user's field it is along the lines of ~user.job_seeker_profile.headline, but for any acccesible field (except password, username, and email which were adapted from the user model)
<hr>

I will handle merges to make sure everything is working
> msg me on teams or we can talk in person if you have any questions
