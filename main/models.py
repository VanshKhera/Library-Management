from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=350)
    author = models.CharField(max_length=300)
    description = models.TextField(max_length=5000, null=True, blank=True)
    issued = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
    
class IssueBook(models.Model):
    
    def pp(self):
        return self.user.pk

    name = models.CharField(max_length=400)
    classSection = models.CharField(max_length=10)
    rollno = models.PositiveIntegerField()
    issued_date = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    # , limit_choices_to={'user' : pp()}

    def __str__(self):
        return f"{self.book} issued by {self.name}"