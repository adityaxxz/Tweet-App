from django.urls import path
from . import views

urlpatterns = [
    #path("admin/", admin.site.urls),
    path('', views.tweet_list, name='tweet_list'),
    path('create/', views.tweet_create, name='tweet_create'),
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    path('register/', views.register, name='register'),
    path('search/', views.tweet_search, name='tweet_search'),
    path('logout/', views.custom_logout, name='logout'),
]




# what does this line do ? 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
# serve user-uploaded media files (such as images, docus, etc.) during development (not in production).