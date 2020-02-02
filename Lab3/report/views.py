from re import search
from urllib import request

from django.shortcuts import HttpResponse, render


# Create your views here.
def show_dashboard(request):
    return HttpResponse('This dashborad!!')

def search_info(request):
    return HttpResponse('Search&Export')
