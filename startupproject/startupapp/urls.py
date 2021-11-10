from django.conf.urls import url
from .views import PublisherList

urlpatterns = [
    url(r'^startups/$', PublisherList.as_view(), name='startup-list')
]
