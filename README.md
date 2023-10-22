# Hello.

This is a template project with django and djoser for users that uses mysql as the database.
It also uses AWS S3 bucket to store and serve files.

# user
The user model is a basic user model that also supports superuser model.
The admin panel provides a good overall admin panel to see all the releavant data in the system.

# Prerequisites

If you want to run it inside docker:
sudo docker-compose build
sudo docker-compose up

Or in local enviroment:
python version: 3.10.10
pip install -r requirements.txt
cd app/
python manage.py migrate
python manage.py runserver

In default - the dev server is running with mysqlite3. But you can add an mysql server in the docker-compose.yml file.

# Urls:

/auth/users/ - POST with:
json```
{
    "username": "email@email.com",
    "passwprd": "somePassword",
    "first_name": "name",
    "last_name": "name",
    "phone_number": "100"
}
```

/auth/jwt/create/ - POST with:
json```
{
    "username": "username",
    "password": "password"
}
```

/auth/users/{user_id} - PUT with:
json```
{
    "field_to_update": "whatever"
}
```