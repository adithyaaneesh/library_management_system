from django.db import models

# Create your models here.
class Library(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    book_type = models.CharField(max_length=100)
    page_no = models.IntegerField()
    added_date = models.DateField(auto_now_add=True)
    publish_date = models.DateField()