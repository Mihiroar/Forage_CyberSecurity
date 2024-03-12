from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("polls/<int:question_id>/", views.detail, name="detail"),
    path("polls/<int:question_id>/results/", views.results, name="results"),
    # Add more URL patterns for other views in the 'polls' app
]
