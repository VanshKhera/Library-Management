# Generated by Django 3.2.5 on 2021-09-30 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_book_issued'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='issued',
            field=models.BooleanField(default=False),
        ),
    ]