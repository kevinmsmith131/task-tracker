# TaskTracker
A task management app that allows users to create a list of tasks, and track which tasks on the list have been completed.

## Features
### Log in Page
The Log in page allows a user to enter a username and password, and then submit this information to be logged in. There is also a link to the Sign up page that a user can follow if they do not have an account yet.

### Sign up Page
The Sign up page allows a user to enter a username, password, confirmation password, and then submit this information to be logged in. There is also a link to the Log in page that a user can follow if they already have an account.

### Task List
### Add Task Page
### Update Task Page
### Delete Task Page

## Technologies
Both the frontend and backend were built using Django, and the backend adheres to RESTful API practices. The data for the application is stored in a PostgreSQL database. The app is deployed to the cloud using Heroku.

## How do I start tracking?
You can access the application using this url: https://heroku-task-tracker.herokuapp.com/

If you would like to see what the app looks like for a user who has already logged some tasks, you can use the demo which has a login of `demo` and a password of `!1234abcd!`. 

If you wish to make your own account, it should be noted that usernames must consist of `alphanumeric`, `_`, `@`, `+`, `.` and `-` characters, and passwords must have `eight` characters, `one` of which must be a `special character`.

When signing up, make sure that the username is a valid username, and the passwords are matching and valid. If all of these conditions are met, and the credentials you are entering are still not working, then try a different username, as there is already an existing user with that username. When logging in, make sure that you are entering the correct username and password.
