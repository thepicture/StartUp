from django.shortcuts import render
from .models import StartUp
from django.views.generic import ListView


class PublisherList(ListView):
    model = StartUp
