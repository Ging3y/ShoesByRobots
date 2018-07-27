from django.http import HttpResponse
from django.shortcuts import render
import operator
from .classes.get_shoe_info import Shoe_DAO

def homepage(request):
    return render(request, 'index.html')

def shoe_info(request):
    link_ = request.GET['shoe_link']
    shoe_info = Shoe_DAO(link_)
    return render(request, 'shoe_info.html', shoe_info.getInfo())
