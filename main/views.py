from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .forms import addBook
from django.http import HttpResponseRedirect

# Create your views here.
global data
data = {
    "form" : addBook(),
    "books" : Book.objects.all()
}
def index(request):
    return render(request, 'index.html', data)

def library(request):
    return render(request, 'library.html', data)

def add_book(request):
    if request.method == "POST":
        form = addBook(request.POST)
        
        if form.is_valid():
            t = form.cleaned_data["title"]
            a = form.cleaned_data["author"]
            m = Book(title=t, author=a)
            m.save()
            return HttpResponseRedirect("/library/")
        else:
            form = addBook()
    return render(request, 'add_book.html', data)

def issue_book(request):
    return render(request, 'issue_book.html', data)