from django import forms 

class addBook(forms.Form):
    title = forms.CharField(label="Title", max_length=350)
    author = forms.CharField(label="Author", max_length=300)