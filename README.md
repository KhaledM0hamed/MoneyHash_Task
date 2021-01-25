# MoneyHash Task

Build an "events" web application where users can log in, create events and sign up for an event and withdraw from an event.
- The UI does not have to look pretty – the focus is on backend development, code quality, and architecture.
- You are free to use any technology or framework on top of Django.
Required Event information: title, description, date

Any user can list events:
- Sorted so that upcoming events are first.
- List view shows title, date and amount of participants.
- List view shows the owner of the event (as the part of the email before the "@").
- Assume there will be many thousands of events, users and participants per event.

Any logged in user can create events.
Logged in users can edit their own events.
Login with email and password.
Registration with email and password.


Out of scope: email confirmation, password reset, change password, profile editing and change email.


## Run locally 

Prerequisites:

- Python3
- docker & docker-compose

Steps:

- `$ docker-compose up` to run the database server
- open [http://localhost:8000/](http://localhost:8000/) to see the app.

Or you can run the app manually:

- `$ pip install -r requirements.txt` to install requirements
- `$ python manage.py runserver` to run the server

Thank you !