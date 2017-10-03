# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	response = "display all users"
	return HttpResponse(response)

def new(request):
	redirect('register')

def register(request):
	response = "create new user"
	return HttpResponse(response)

def login(request):
	response = "users login"
	return HttpResponse(response)