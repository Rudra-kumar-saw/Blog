from django.shortcuts import render

# Create your views here.
def chai_all(request):
    return render(request,'chai/chai_all.html')