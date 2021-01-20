# INSTAGRAM-CLONE
## Author
[Preston-Too](https://github.com/Preston-Too)

## Live Link
* [here] ()

## Description
 Instagram-clone is an application developed using Django. This is an application that allows users to sign up, upload pictures,view other user's pictures,like them, comment on them and also follow the other users.

## Setup and installations
* Clone Project to your machine
* Activate a virtual environment on terminal: source virtual/bin/activate
* Install all the requirements found in requirements.txt file.
* On your terminal run python3.6 manage.py runserver
* Access the live site using the local host provided

## Getting started

#### The application requires the following installations to operate 
* python3.6
* virtual environment
* pip

#### Cloning

* Open Terminal {Ctrl+Alt+T}

* git clone ```https://github.com/Preston-Too/Instagram-Clone.git```

* Create and activate the virtual environment
    ```python3.6 -m virtualenv virtual```
    ```source virtual/bin/activate```

* Move to the folder and install requirements
    ```pip install -r requirements.txt```

## Setting up environment variables
Create a .env file and paste paste the following filling where appropriate:

* SECRET_KEY='Generate one that suits you'
* DEBUG=True
* DB_NAME='gallery'
* DB_USER='<your database name>'
* DB_PASSWORD='<password to your database>'
* DB_HOST='127.0.0.1'
* MODE='dev'
* ALLOWED_HOSTS='*'
* DISABLE_COLLECTSTATIC=1

## Make and run migrations
* python3.6 manage.py check
* python manage.py makemigrations 
* python3.6 manage.py sqlmigrate instagram 0001
* python3.6 manage.py migrate

## Run the app
* Running the application
    ```python3.6 manage.py runserver```
* Testing the application
    ```python3.6 manage.py test```

## Technologies Used

* python3.8
* Django
* Postgresql
* Bootstrap
* HTML / CSS

## User Stories
As a user of the application I should be able to:

* Sign in to the application to start using.
* Upload my pictures to the application.
* See my profile with all my pictures.
* Follow other users and see their pictures on my timeline.
* Like a picture and leave a comment on it.

## Known Bugs
* There are no known bugs at the moment

## Contact Information 

If you have any question or contributions, please email me at [toopreston@gmail.com]

## License
* [[License: MIT]](LICENCE.md)
* Copyright (c) 2020 **Preston Too**