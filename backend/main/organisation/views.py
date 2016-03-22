from django.shortcuts import render
from django.http import HttpResponse
from main.models import Organisation
import json

def index(request):
    return HttpResponse("Hello, world.")

def create(request, id):
    response = "You've created id %s"
    return HttpResponse(response % id)

def read(request, id):
    organisation = Organisation.objects.get(id='%s' % id)
    response = json.dumps(organisation.as_json())
    return HttpResponse(response, content_type='application/json')

def update(request, id):
    response = "You've updated id %s"
    return HttpResponse(response % id)

def delete(request, id):
    response = "You've readed id %s"
    return HttpResponse(response % id)
