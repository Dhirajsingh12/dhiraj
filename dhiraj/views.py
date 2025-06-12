from service.models import service
from django.shortcuts import render
def hp(request):
    data={'title':'newtitle django','number':[12,45,3,5,24,24]}
    return render(request,'index.html',data)
from django.http import HttpResponse
def aboutme(request):
    return HttpResponse("welcome to django view")
from django.http import HttpResponse
from django.shortcuts import render, redirect

def loginUser(request):
    username = "dhiraj"
    password = "Kumar@2004"
    userLoggedIn = ""

    if request.method == "GET":
        try:
            username1 = request.GET('username')
            password1 = request.GET('password')

            if (username == username1) and (password == password1):
                userLoggedIn="successfully login"
                return redirect('/loggedIn')
            else:
                userLoggedIn = "Invalid username or password"
                print(userLoggedIn)
        except Exception as e:
            userLoggedIn = f"Error: {str(e)}"

    return render(request, "login_user.html", {"isUserLoggedIn": userLoggedIn})

def loggedInUser(request):
    return render(request, "landing_page.html")
def load(request):
    serviceData = service.objects.all()
    '''
    for a in serviceData:
        print(a.service_ID)
        print(a.service_Title)
        print(a.service_Desc)
    print(service1)
    '''
    return render(request, 'load.html', {'service': serviceData})