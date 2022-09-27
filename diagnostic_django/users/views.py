from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view
from .models import User
# Create your views here.

@api_view(['POST,PUT'])
def userRegistration(request):
    pass

def user_obj(request):
    users  = User.objects.all()
    print(users[0])
    return HttpResponse("aish")