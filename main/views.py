from django.conf import settings
from django.shortcuts import redirect, render
from .models import Book, IssueBook
from .forms import BookForm, issueBook
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

User = settings.AUTH_USER_MODEL

@login_required(login_url='login')
def index(request):
    upcoming_dues = IssueBook.objects.all().filter(user=request.user).order_by('date')
    recent_books = Book.objects.all().filter(user=request.user).order_by('creation_date')

    d = {
        'dues' : upcoming_dues,
        'books' : recent_books
    }
    return render(request, 'index.html', d)

@login_required(login_url='login')
def library(request):
    return render(request, 'library.html', {'books' : Book.objects.filter(user=request.user)})

@login_required(login_url='login')
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)

        if form.is_valid():
            a = form.save()
            a.user = request.user
            a.save()
            return HttpResponseRedirect("/book/%d" % a.id)
        else:  
            form = BookForm()
    return render(request, 'add_book.html', {"form" : BookForm()})

@login_required(login_url='login')
def issue_book(request):
    if request.method == 'POST':
        issueForm = issueBook(request.POST, usr=request.user)
        if issueForm.is_valid():
            issueForm.user = request.user
            issued = issueForm.save()

            if issued.book.issued == True:
                issued.delete()
                messages.warning(request, "Book already issued to someone, retrieve it to issue it to someone else again.")

            else:
                current_book = issued.book
                print(current_book)
                current_book.issued = True
                current_book.save()
                return redirect('/books-issued')
    else: 
        issueForm = issueBook(usr = request.user)          
    return render(request, 'issue_book.html', {'issue_book_form': issueBook(usr = request.user)})
    
@login_required(login_url='login')
def book(request, id):
    ls = Book.objects.get(id=id, user=request.user)
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
    issued = IssueBook.objects.filter(user=request.user)
    books = Book.objects.filter(issued=True, user=request.user)
    print(issued, books)
    context = { 
        "books" : books,
        "issued" : issued
    }
    return render(request, 'books_issued.html', context)

@login_required(login_url='login')
def issueEdit(request, id):
    current_data = IssueBook.objects.get(id=id)
    form = issueBook(instance=current_data, usr=request.user)
    
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

@login_required(login_url='login')
def deleteIssue(request, id):
    if request.method == 'POST':
        issue = IssueBook.objects.get(book=Book.objects.get(pk=id))
        issue.book.issued = False
        issue.book.save()
        issue.delete()
        return redirect("/books-issued/")
    return render(request, 'issue_delete.html')

@login_required(login_url='login')
def retrieveBook(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        a = IssueBook.objects.get(book=Book.objects.get(pk=id))
        a.book.issued = False
        a.book.save()
        a.delete()
        messages.info(request, "Book retrieved successfully!")
        return redirect('/books-issued')
    return render(request, 'retreive.html', { 'data' : book })