from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('footer', views.footer, name='footer'),
    path('contact', views.contact, name='contact'),
    path('contact1', views.contact1, name='contact1'),
]
