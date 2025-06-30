# django notes

## create a new project
django-admin startproject tweet-app

## create a new app
python .\manage.py startapp tweet

## activate virtual environment
.\.venv\Scripts\activate

## run server 
python .\manage.py runserver

## create admin aka superuser
python .\manage.py createsuperuser

django-admin startproject tweet-app



python .\manage.py makemigrations tweet
 python .\manage.py migrate

---


# The search functionality is just a form — the data will come from inside the form. Based on that data, Django's ORM will be used to perform a search, specifically on the basis of tweet text. Then, a new view needs to be created, and also a new template for displaying the search results.




