from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=350)
    author = models.CharField(max_length=300)
    description = models.TextField(max_length=5000, null=True, blank=True)
    issued = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} by {self.author}"
    
class IssueBook(models.Model):
    name = models.CharField(max_length=400)
    classSection = models.CharField(max_length=10)
    bookName = models.ForeignKey(Book, on_delete=models.CASCADE)
    rollno = models.PositiveIntegerField()
    issued_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    
    def __str__(self):
        return f"{self.name} issued {self.bookName}"