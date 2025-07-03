from django.contrib import admin
from .models import Tweet, Comment

# Register your models here. after creating models, you need to register them in the admin site. to be able to see them in admin

class TweetAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'text')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'tweet', 'text', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'text')


admin.site.register(Tweet, TweetAdmin)
admin.site.register(Comment, CommentAdmin)
