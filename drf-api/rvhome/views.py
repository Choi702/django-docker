from django.shortcuts import render
from rest_framework import generics
from .serializer import rvhomeSerializer
from .models import rvhome


class rvhomeList(generics.ListCreateAPIView):
    queryset = rvhome.objects.all()
    serializer_class = rvhomeSerializer

class rvhomeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = rvhome.objects.all()
    serializer_class = rvhomeSerializer


# Create your views here.

    