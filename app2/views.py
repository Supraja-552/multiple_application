from django.shortcuts import render
from django.http import HttpResponse

def first1(request):
    return render(request,'index2.html')
def second1(request):
    return HttpResponse('<h1> this is second function of second applicaton')
