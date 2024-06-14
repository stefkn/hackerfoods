from django.urls import path
from hackerfoods_app import views

app_name = "hackerfoods_app"

urlpatterns = [
    path("", views.recipes, name='recipes'),
    path("about", views.about, name='about'),
    path("<int:recipe_id>/", views.detail, name="detail"),
]
