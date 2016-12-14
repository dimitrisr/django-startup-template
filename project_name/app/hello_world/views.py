# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

def hello(request):
    return render(request, 'hello_world.html', locals())