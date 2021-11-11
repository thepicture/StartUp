from django.shortcuts import render
from .models import StartUp
from django.views.generic import ListView, View


class PublisherList(ListView):
    model = StartUp

class HomeView(View):
    template_name = ''