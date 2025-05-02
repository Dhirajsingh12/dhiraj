from django.shortcuts import render
def hp(request):
    data={'title':'newtitle django','number':[12,45,3,5,24,24]}
    return render(request,'index.html',data)
from django.http import HttpResponse
def aboutme(request):
    return HttpResponse("welcome to django view")
