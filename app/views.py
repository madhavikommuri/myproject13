from django.shortcuts import render

# Create your views here.

def heaven(request):
    return render(request,'heaven.html')