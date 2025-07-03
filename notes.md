## django structure

> User -> request -> urls.py -> views.py -> templates -> response

or, a verbose way to put it:

![django structure](/django-structure.png)

## django cmds

### - create a new project
```django-admin startproject tweet-app```

### - create a new app
```python .\manage.py startapp tweet```

### - activate virtual environment
```.\.venv\Scripts\activate```

### - run server 
```python .\manage.py runserver```

### - create admin aka superuser
```python .\manage.py createsuperuser```

### - make migrations
```python .\manage.py makemigrations tweet```

### - migrate
```
python .\manage.py makemigrations tweet
python .\manage.py migrate
```

---


- The search functionality is just a form — the data will come from inside the form. Based on that data, Django's ORM will be used to perform a search, specifically on the basis of tweet text. Then, a new view needs to be created, and also a new template for displaying the search results.


- the comments functionality is working, created a new model for the comments and a comment form and then added it to views. added the url for the comments. then a new template for the comments using django forms [tweet_detail.html](tweetapp/tweet/templates/tweet_detail.html)
registered this comment model in the admin so that admin can view all the comments.

