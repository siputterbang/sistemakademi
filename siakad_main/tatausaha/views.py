from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def landingTU(req):
    context={

    }
    return HttpResponse('hallo,ini halaman tatausaha')

def login(req):
    return render(req,'login.html')

