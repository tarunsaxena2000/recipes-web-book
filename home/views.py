from django.shortcuts import render
from django.http import HttpResponse


peoples =[
   {"name":"tarun saxena", "age":20},
     {"name":"atin saxena", "age":22},
       {"name":"rashu saxena", "age":15},
         {"name":"robin saxena", "age":45},
           {"name":"anubhav saxena", "age":34},
]


def home(request):
    return render(request , "index.html",context={'peoples' : peoples})


def success_page(request):
    return HttpResponse("hey this the second sucess page")
