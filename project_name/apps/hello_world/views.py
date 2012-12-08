# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

def hello(request):
    return render_to_response('hello_world.html',
        locals(), context_instance = RequestContext(request))
