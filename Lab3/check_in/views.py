from http.client import HTTPResponse
from urllib import request

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def welcome(request):
    return HttpResponse("Detaill of subject for teacher!")

def course(request, id):
    return HttpResponse("Course ID is %d" %id)

def QRcode(request):
    return HttpResponse("Scan this...for check in!")