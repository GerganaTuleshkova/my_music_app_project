from django.contrib import admin
from django.urls import path

from exam_project.exam_app.views import home, album_add, album_details, album_edit, album_delete, profile_details, \
    profile_delete

urlpatterns = [
    path('', home, name='home'),
    path('album/add/', album_add, name='album add'),
    path('album/details/<int:pk>/', album_details, name='album details'),
    path('album/edit/<int:pk>/', album_edit, name='album edit'),
    path('album/delete/<int:pk>/', album_delete, name='album delete'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/delete/', profile_delete, name='profile delete'),
]
