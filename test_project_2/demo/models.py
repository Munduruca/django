from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=36, unique=True)
    description = models.TextField(max_length=256, 
                                   default=None)