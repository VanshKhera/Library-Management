from django.contrib import admin
from main.models import Book, IssueBook, user

# Register your models here.
admin.site.register(Book)
admin.site.register(IssueBook)
admin.site.register(user)