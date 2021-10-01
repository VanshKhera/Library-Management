from django import forms
from django.forms import widgets, ModelForm 
from .models import Book, IssueBook

"""class addBook(forms.Form):
    title = forms.CharField(label="Title", max_length=350)
    author = forms.CharField(label="Author", max_length=300)
    description = forms.CharField(label="Description", widget=forms.Textarea(
        attrs={
            'placeholder': "Description (optional)",
            'rows' : 4
            }
    ))"""
    
"""class issueBook(forms.Form):
    name = forms.CharField(max_length=400, label="Student Name")
    classSection = forms.CharField(max_length=10, label="Class & Section")
    rollno = forms.CharField(label="Roll No.")
    # bookName = forms.ChoiceField
    due_date = forms.DateField(label="Due Date")"""
    
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']

class issueBook(ModelForm):
    class Meta:
        model = IssueBook
        fields = '__all__'