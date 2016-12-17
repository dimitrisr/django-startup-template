# -*- coding: utf-8 -*-

from django.shortcuts import render

def hello(request):
    return render(request, 'hello_world.html', locals())