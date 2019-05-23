from django.shortcuts import render
from django.http import HttpResponse

def home(request):
   text = """<h1>This is our home page!</h1>"""
   return HttpResponse(text)