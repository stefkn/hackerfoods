from django.urls import path
from hackerfoods_app import views

urlpatterns = [
    path("", views.home, name='home'),
    path("about", views.about, name='about'),
    path("<int:recipe_id>/", views.detail, name="detail"),
]
