from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class AnotherClass(View):
    def get(self, request):
        return HttpResponse('My message from the class')



def first(request):
    return HttpResponse('First message from views')
