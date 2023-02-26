# ToDoListDjango

## Description of the project
The project ToDoListDjango contains Web-app of ToDoList appliction. The app will shortly be able to create, save, edit and delete your projects with tasks 
which will let you organize your work on any project or simply make timetable for your day. The app uses Django framework.

## Navigation
1. The repository structure is:
  - todolist
    - todolist
      - asgi.py  
      - __init__.py 
      -  __pycache__  
      - settings.py  
      -  urls.py  
      -  wsgi.py
   - todolistapp
      - admin.py  
      -  apps.py  
      -  forms.py   - **Forms classes**
      -  __init__.py 
      -  migrations - **Contains migration files**
      -  models.py  - **Database models**
      -  __pycache__  
      -  templates  - **Contains html templates**
      -  tests.py  
      -  urls.py    - **Urls connecting to views**
      -  views.py   - **Views of pages**
    - db.sqlite3
    - manage.py

## Luching app
To luch the app copy this repository on your PC. Make sure you have installed Django framework and Python. Open the todolist directory on your terminal
and write the following command: 
```
python3 manage.py runserver 
```
Than follow the link which was given and use the application.
