# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	response = "display all blogs"
	return HttpResponse(response)

def new(request):
	response = "create new blog"
	return HttpResponse(response)

def create(request):
	return redirect('/')

def show(request):
	response = "display blog {{number}}"
	return HttpResponse(response)

def edit(request):
	response = "edit blog {{number}}"
	return HttpResponse(response)

def destroy(request):
	return redirect('/')