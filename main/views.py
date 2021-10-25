from django.shortcuts import redirect, render
from .models import Book, IssueBook
from .forms import BookForm, issueBook
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
global data
data = {
    "issue_book_form" : issueBook,
    "form" : BookForm(),
    "books" : Book.objects.all(),
}
def index(request):
    return render(request, 'index.html', data)

@login_required(login_url='login')
def library(request):
    data['books'] = Book.objects.all()
    return render(request, 'library.html', data)

@login_required(login_url='login')
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

@login_required(login_url='login')
def issue_book(request):
    if request.method == 'POST':
        issueForm = issueBook(request.POST)

        if issueForm.is_valid():         
            issued = issueForm.save()   
            current_book = issued.bookName
            current_book.issued = True
            current_book.save()
            return redirect('/books-issued')
    else:
        issueForm = issueBook()
    return render(request, 'issue_book.html', data)

@login_required(login_url='login')
def book(request, id):
    ls = Book.objects.get(id=id)
    return render(request, 'book.html', {"ls" : ls})
@login_required(login_url='login')
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

@login_required(login_url='login')
def deleteBook(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.delete()        
        return redirect('/library')
    context = {
        "book" : Book.objects.get(id=id)
        }
    return render(request, 'delete_book.html', context)

@login_required(login_url='login')
def booksIssued(request):
    if request.method == 'POST':
        try:    
            if request.POST.get("take_back"):
                print(":O")
        except:
            print("FAIL LOL")
    issued = IssueBook.objects.all()
    context = { 
        "books" : Book.objects.all().filter(issued=True),
        "issued" : issued
    }
    return render(request, 'books_issued.html', context)

@login_required(login_url='login')
def issueEdit(request, id):
    current_data = IssueBook.objects.get(id=id)
    form = issueBook(instance=current_data)
    
    if request.method == "POST":
        if request.POST.get('return_book'):
            pass
        form = issueBook(request.POST, instance=current_data)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form" : form
    }
    return render(request, 'issue_update.html', context) 

def deleteIssue(request, id):
    issue = IssueBook.objects.get(id=id)
    if request.method == 'POST':
        issue.delete()
        return redirect("/books-issued/")
    context = {
        "issue" : issue
    }
    return render(request, 'issue_delete.html', context)