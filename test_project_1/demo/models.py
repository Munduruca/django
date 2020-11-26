from django.db import models


class Book(models.Model):
    
    title = models.CharField(max_length=36)
    # reading_status = models.CharField(max_length=36,
    #                                   #blank=False,
    #                                   #default=1,
    #                                   #choices=STATUSES
    #                                   )
    # description = models.TextField(max_length=512, 
    #                                blank=True)
    # price = models.DecimalField(default=0,
    #                             decimal_places=2,
    #                             max_digits=10)
    # published = models.DateField(blank=True, default=None)
    # acquired = models.DateTimeField(auto_now=True)
    # cover = models.FileField(upload_to='covers/',
    #                          blank=True)
    # is_gift = models.BooleanField(default=False)