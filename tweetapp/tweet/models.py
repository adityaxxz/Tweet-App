from django.db import models
from django.contrib.auth.models import User #importing user model
from django.utils import timezone

# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #user is a foreign key to the user model
    # on_delete=models.CASCADE means If a User is deleted, all Tweet objects related to that user will also be deleted automatically.

    text = models.TextField(max_length=280)

    photo = models.ImageField(upload_to='photos/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add=True means the field will be automatically set to the current date and time when the object is created.

    updated_at = models.DateTimeField(auto_now=True) #auto_now=True means the field will be automatically updated to the current date and time when the object is updated.

    date = models.DateField(default=timezone.now) #null=True means the field can be empty, blank=True means the field can be empty when creating a new object.
    
    # Many-to-many relationship with User for likes
    likes = models.ManyToManyField(User, related_name='liked_tweets', blank=True)

    #this is what we see in our admin panel
    #http://127.0.0.1:8000/admin/tweet/tweet/
    def __str__(self):
        return f"{self.user.username} - {self.text}" 
    
    # Method to get the total number of likes
    def total_likes(self):
        return self.likes.count()
        
    # Method to get all comments for this tweet
    def get_comments(self):
        return self.comments.all().order_by('-created_at')
        
    class Meta:
        ordering = ['-created_at']  # Default ordering newest first

# One to many relationship: (one tweet can have many comments)
class Comment(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='comments') 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.text}" 
        
    class Meta:
        ordering = ['-created_at']  # Default ordering newest first

# One to one relationship: (one user has one profile)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=150, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.bio}" 
    