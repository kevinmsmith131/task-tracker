# TaskTracker
A task management app that allows users to create a list of tasks, and track which tasks on the list have been completed.

## Features
### Log in Page
The Log in page allows a user to enter a username and password, and then submit this information to be logged in. There is also a link to the Sign up page that a user can follow if they do not have an account yet.

### Sign up Page
The Sign up page allows a user to enter a username, password, confirmation password, and then submit this information to be logged in. There is also a link to the Log in page that a user can follow if they already have an account.

### Task List
#### Header
The header displays a greeting to the signed in user. Below the greeting is a message that displays the number of incomplete tasks. The word "Logout" is present in the top right corner, and when it is clicked, the signed in user is logged out.

#### Search and Add Area
When a user enters a phrase into the search bar, and hits search, only the tasks that start with that phrase are displayed on the task list. When the plus icon is clicked, the user is brought to the add task page.

#### Tasks
Each task has a completed status indicator, which is a green circle when the task has been completed, and a gray circle when the task has not been completed. When this circle is clicked, the completed status of the task is toggled to the opposite of what it previously was. Each task also has a title, which is italicized and struckthrough if the task is complete, and has no effect if it is not complete. When the title of the task is clicked, the user is brought to the update task page. There is also a red delete icon, which when clicked, brings the user to the delete page for the task. As a side note the tasks are ordered so that the completed tasks are on the bottom, and the uncompleted tasks are on the top.

### Add Task Page
The user is able to go back to the task list by pressing the back button, if they no longer wish to add a task. Otherwise, the user is able to enter the title of the new task, a description of the new task, and then submit this information to be added to the task list.

### Update Task Page
The user is able to go back to the task list by pressing the back button, if they no longer wish to update the selected task. Otherwise, the user is able to change the title and description of the task, and then submit this updated task to replace the old task on the task list. The update task page can also be used as a way to view the description of the task for users wishing to find out more about the task.

### Delete Task Page
The delete task page allows a user to go back to the task list if they do not want to delete the selected task, or press confirm if they do wish to delete the task.

## Technologies
Both the frontend and backend were built using Django, and the backend adheres to RESTful API practices. The data for the application is stored in a PostgreSQL database. The app is deployed to the cloud using Heroku.

## How do I start tracking?
You can access the application using this url: https://heroku-task-tracker.herokuapp.com/

If you would like to see what the app looks like for a user who has already logged some tasks, you can use the demo which has a login of `demo` and a password of `!1234abcd!`. 

If you wish to make your own account, it should be noted that usernames must consist of `alphanumeric`, `_`, `@`, `+`, `.` and `-` characters, and passwords must have `eight` characters, `one` of which must be a `special character`.

When signing up, make sure that the username is a valid username, and the passwords are matching and valid. If all of these conditions are met, and the credentials you are entering are still not working, then try a different username, as there is already an existing user with that username. When logging in, make sure that you are entering the correct username and password.
