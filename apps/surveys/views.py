# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	response = 'all surveys'
	return HttpResponse(response)

def new(request):
	response = 'add new survey'
	return HttpResponse(response)