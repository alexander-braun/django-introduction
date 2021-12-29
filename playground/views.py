from django.shortcuts import render
from django.http import HttpResponse

# takes request -> returns response
# request handler

def say_hello(request):
  # Pull data from db
  # transform data
  # send email 
  # ...
  return render(request, 'hello.html', { 'name': 'Alex' })