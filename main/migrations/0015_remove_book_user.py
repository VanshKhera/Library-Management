# Generated by Django 3.2.5 on 2021-10-25 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_book_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='user',
        ),
    ]