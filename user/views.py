from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def user_page(request):
    return HttpResponse("This will be the user page")