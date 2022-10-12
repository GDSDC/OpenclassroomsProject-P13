from django.contrib import admin
from django.urls import path

from oc_lettings_site.profiles import views

urlpatterns = [
    path('profiles/', views.profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', views.profile, name='profile'),
]