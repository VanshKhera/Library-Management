from django import forms
from django.forms import widgets, ModelForm 
from .models import Book, IssueBook

    
class BookForm(ModelForm):
    # description = forms.Textarea(widget=forms.TextInput(attrs={'placeholder': 'Description (optional)',}))
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']

class issueBook(ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('usr')
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['book'] = forms.ModelChoiceField(queryset=Book.objects.filter(user = user))

    date = forms.DateTimeField(widget=forms.DateInput(attrs={'type':'date'}))

    class Meta:
        model = IssueBook
        fields = ['name', 'classSection', 'book', 'rollno', 'date'] 