from django.db import models
from django.contrib.auth.models import User #importing user model


# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #user is a foreign key to the user model
    # on_delete=models.CASCADE means If a User is deleted, all Tweet objects related to that user will also be deleted automatically.

    text = models.TextField(max_length=280)

    photo = models.ImageField(upload_to='photos/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add=True means the field will be automatically set to the current date and time when the object is created.

    updated_at = models.DateTimeField(auto_now=True) #auto_now=True means the field will be automatically updated to the current date and time when the object is updated.

    def __str__(self):
        return f"{self.user.username} - {self.text}"
    




    