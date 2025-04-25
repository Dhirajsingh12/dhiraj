from django.http import HttpResponse
def aboutme(request):
    return HttpResponse("welcome to django view")