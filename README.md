# ToDo App

The goal of the following assignment is to write a simple ToDo app. The first part will consist only
on writing backend, then we’ll try to create simple single page app for it.

### Note
Clone this repository to start working on the task. Commit often :)

## Run instructions
With docker installed on your machine you should just simply run `./run.sh` and everything should
setup automatically. Frontend is available under `http://localhost:3000` and backend under
`http://localhost:3000/api/`

## Part 1
Using Flask, Python and MongoDb write a simple backend that will allow user to:
- Add new To Do item
- Fetch all todo items
- Mark todo item as done
- Unmark todo item as done
- Delete an item
- Update item text

For now we can assume that there is only one user in the system. We'll add authentication later.

Design API according to REST architecture, write simple documentation in Markdown.

## Part 2
Write simple frontend (without using any frontend frameworks) that will allow user to see his todos,
add, edit, update and delete them (basically frontend that will use all backend functionalities).

## Part 3
Extend both backend and frontend with the following functionalities:
1. Add ability to assigning priority to tasks. Sort tasks on the frontend according to their
priority.
2. Add search functionality on the frontend side - user should be able to filter in real time his
tasks.
3. Add functionality to add labels for tasks and ability to display only tasks under specific label.
Backend should be able to return only tasks for a specific label defined as a query parameter.
4. Add ability to register, login in the system. User should be able to add and see only his tasks.
All other functionality should stay intact.
5. Add ability to login using Facebook identity (OAuth).i


Happy Coding :)
