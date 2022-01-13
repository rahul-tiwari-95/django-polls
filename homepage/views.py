from django.http import HttpResponse, response
from django.shortcuts import render


def home(self):
    return HttpResponse("hey")