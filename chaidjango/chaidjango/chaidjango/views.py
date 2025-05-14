from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'website/index.html')
    # return HttpResponse("hello,world .you are at chai aur code home page")
    

def about(request):
    return HttpResponse("hello,world .you are at chai aur code about page")


def contact(request):
    return HttpResponse("hello,world .you are at chai aur code conatact page")




