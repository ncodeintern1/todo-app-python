from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import userform
# Create your views here.
def index(request):
    return render(request,"index.html")


def user(request):
    forms =userfrom(request.POST)
    if forms.is_valid():
        forms.save()
        return redirect('index')
    else:
        print("is in valid")
    return render(request,"index.html",{'forms':forms})