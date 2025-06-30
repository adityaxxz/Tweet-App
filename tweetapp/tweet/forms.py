from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#why we create forms? 

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2') #using a tuple to specify the fields, rather than an array like above coz we're using built in forms.


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)
    

