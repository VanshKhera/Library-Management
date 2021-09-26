from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("library/", views.library, name="library"),
    path("add-book/", views.add_book, name="add_book"),
    path("issue-book/", views.issue_book, name="issue_book"),
]
