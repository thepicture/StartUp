from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from .views import HomeView, StartUpListView

urlpatterns = [
    url(r'^home/$', HomeView.as_view(), name='home-view'),
    url(r'^startups/$', StartUpListView.as_view(), name='startup-list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)