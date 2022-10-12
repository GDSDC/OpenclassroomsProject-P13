from django.contrib import admin
from django.urls import path

from oc_lettings_site.lettings import views

app_name = 'lettings'
urlpatterns = [
    path('lettings/', views.lettings_index, name='index'),
    path('lettings/<int:letting_id>/', views.letting, name='letting'),
]
