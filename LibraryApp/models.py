from django.db import models

# Create your models here.
class Library(models.Model):
    book_name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    book_type = models.CharField(max_length=30)
    page_no = models.IntegerField(max_length=30)
    added_date = models.DateField()
    publish_date = models.DateField()