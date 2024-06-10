from django.urls import path
from hackerfoods_app import views

urlpatterns = [
    path("", views.home, name='home'),
]
