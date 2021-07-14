from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('login/', loginpage, name='loginpage'),
    path('register/', registerpage, name='signuppage'),
    path('logout/', signout, name='logoutpapge'),
    path('dashboard/', myaccount, name='dashboard'),
    path('invest-now/', invest, name='invest'),
    path('complete-payment/', compelteinvestment, name='compeleteinvestment'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)