from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("library/", views.library, name="library"),
    path("add-book/", views.add_book, name="add_book"),
    path("issue-book/", views.issue_book, name="issue_book"),
    path("book/<int:id>", views.book, name="individual_book"),
    path("update/<int:id>", views.updateBook, name="update_book"),
    path("delete/<int:id>", views.deleteBook, name="delete_book"),
    path("books-issued/", views.booksIssued, name="books_issued"),
    path("issue/edit/<int:id>", views.issueEdit, name="issue_edit"),
    path("issue/delete/<int:id>", views.deleteIssue, name="issue_delete"),
    path("retrieve-book/<int:id>", views.retrieveBook, name="retrieve_book")
]
