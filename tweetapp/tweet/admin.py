from django.contrib import admin
from .models import Tweet

# Register your models here. after creating models, you need to register them in the admin site. to be able to see them in admin

admin.site.register(Tweet)
