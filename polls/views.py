from django.http import HttpResponse, response

def index(request):
    response = "hello world, you're on Index"
    return HttpResponse(response)


def detail(request, question_id):
    response = "You're looking at question %s."
    return HttpResponse(response % question_id)


def results(request,question_id):
    response = "These are results for question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    response = "You're voting on question %s."
    return HttpResponse(response % question_id)
