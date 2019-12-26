from django.shortcuts import render
from django.http import JsonResponse
from .models import Token
from django.contrib.auth import authenticate
import uuid

# Create your views here.
def login(request):
    password=request.GET["password"]
    username = request.GET["username"]
    user = None
    token = ''
    user = authenticate(username=username, password=password)
    obj, _ = Token.objects.get_or_create(user=user, defaults={
        "token": str(uuid.uuid1())
    })
    token = obj.token

    return JsonResponse({"token": token})