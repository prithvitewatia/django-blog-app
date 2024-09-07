# Create your views here.
from django.shortcuts import render


def gateway(request):
    return render(request, 'gateway/gateway.html')