from django.http import HttpResponse, response

def home(request):
    response = "Welcome to the homepage"
    return HttpResponse(response)