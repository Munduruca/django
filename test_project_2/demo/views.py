from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book

class AnotherClass(View):

    books = Book.objects.get(id=2)
    #for i in books:
    output = books.title

    def get(self, request):
        return HttpResponse(self.output)

def first(request):
    return HttpResponse('First message from views')
