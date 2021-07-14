from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', main, name='homepage'),
    path('about/', about, name='aboutus'),
    path('investment/', investments, name='investmentplan'),
    path('faqs/', faqs, name='faqs'),
    path('ratings/', ratings, name='ratings'),
    path('support/', support, name='support'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)