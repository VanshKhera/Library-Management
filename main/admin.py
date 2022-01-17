from django.contrib import admin
from main.models import Book, IssueBook
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
admin.site.register(Book)
admin.site.register(IssueBook)