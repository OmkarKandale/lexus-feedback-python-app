1. Create a folder called feedbackApp

2. Install pipenv using
   pip instal pipenv

3. Run command
   pipenv shell
   It will create a pipfile which store our packages and python version

pipenv install flask ---web-framework

pipenv install psycopg2 ---database adapter inorder to work with postgrtes

pipenv install psycopg2-binary ---same as above only if above is not worked

pipenv install flask-sqlalchemy ---abstract for working with database like mongoose and allows to create databse models and schemas

pipenv install gunicorn ---it is server like httpsever we need this when we depoly to heroku

Create folders static and templates

create logo and stylesheet in the static folder

create index.html and success.html in templates folder

create app.py in the main directory of the app

openterminal and type following commands
python
from app import db
db.create_all()

- use add user name and password in the URI
  This will create the table in the pgadmin 4

create send_mail.py add username and password from mailtrap

update in app.py

download heroku cli
check --> heroku --version

login on heroku
heroku login

create a app
heroku create app-name
\*app-name should be universaly unique

add postgresql addon to the app
heroku addons:create heroku-postgresql:hobby-dev --app app-name

for production changing DATABASE URI from local heroku DATABASE URL
heroku config --app app-name
this will give as the DATABASE url

change ENV in the app.py to 'prod' and URI to production url

create a Procfile
touch Procfile

open Procfile and
web: gunicorn app: app

create a file runtime.txt
python-major.minor.patch
for python version
python -v

create requirements.txt file using
pip freeze > requirements.txt

create a local git repository
git add .
add comment to the repository
git commit -m "comment"

to deploy on heroku
heroku git:remote -a lexus-feedback-python-app

push to heroku
git push heroku master

to open the app
heroku open
