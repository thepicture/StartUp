from .models import StartUp
from django.views.generic import ListView, TemplateView


class StartUpListView(ListView):
    model = StartUp


class HomeView(TemplateView):
    template_name = 'startupapp/home.html'
