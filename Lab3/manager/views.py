from http.client import HTTPResponse
from urllib import request

from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def show_listname(request):
    return HttpResponse("Listname Student!")

def show_add(request):
    return HttpResponse("Add Student!!")

def show_edit(request):
    return HttpResponse("Edit list!!!")

def show_listSubject(request):
    return HttpResponse("listname Subject!!!!")

def show_addSubject(request):
    return HttpResponse("Add Subject!!!!!")

def show_editSubject(request):
    return HttpResponse("Edit Subject!!!!!!")
