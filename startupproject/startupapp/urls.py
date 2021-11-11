from django.conf.urls import url
from .views import HomeView, PublisherList

urlpatterns = [
    url(r'^home/$', HomeView.as_view(), name='home-view'),
    url(r'^startups/$', PublisherList.as_view(), name='startup-list')
]
