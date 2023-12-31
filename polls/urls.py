from django.urls import path

from . import views

urlpatterns = [
        # ex: /polls/
    path("", views.index, name="index"),
        # ex: /polls/1
    path("<int:question_id>", views.detail, name="detail"),
    path("<int:question_id>/results", views.results, name="results"),
    path("<int:question_id>/vote", views.vote, name="vote"),
    
]
