from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Book, IssueBook
from .forms import BookForm, issueBook
from django.http import HttpResponseRedirect

# Create your views here.
global data
data = {
    "issue_book_form" : issueBook,
    "form" : BookForm(),
    "books" : Book.objects.all(),
}
def index(request):
    return render(request, 'index.html', data)

def library(request):
    data['books'] = Book.objects.all()
    return render(request, 'library.html', data)

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        
        if form.is_valid():
            t = form.cleaned_data["title"]
            a = form.cleaned_data["author"]
            d = form.cleaned_data["description"]
            m = Book(title=t, author=a, description=d)
            m.save()
            return HttpResponseRedirect("/book/%d" % m.id)
        else:
            form = BookForm()
    return render(request, 'add_book.html', data)

def issue_book(request):
    if request.method == 'POST':
        issueForm = issueBook(request.POST)
        
        if issueForm.is_valid():
            n = issueForm.cleaned_data["name"]
            class_sec = issueForm.cleaned_data["classSection"]
            rollno = issueForm.cleaned_data["rollno"]
            bookname = issueForm.cleaned_data["bookName"]
            dueDate = issueForm.cleaned_data["due_date"]
            # Book.objects.issued = True
            d = IssueBook(name=n, classSection=class_sec, rollno=rollno, bookName=bookname, due_date=dueDate)
            d.save()
            return redirect('/')
    else:
        issueForm = issueBook()
    return render(request, 'issue_book.html', data)

def book(request, id):
    try:
        ls = Book.objects.get(id=id)
        return render(request, 'book.html', {"ls" : ls})
    except:
        return render(request, 'not_found.html')

def updateBook(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(instance=book)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("/book/%d" % book.id)
        
    context = {
        'form': form
        }
    return render(request, 'update_book.html', context)

def deleteBook(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.delete()        
        return redirect('/library')
    context = {
        "book" : Book.objects.get(id=id)
        }
    return render(request, 'delete_book.html', context)