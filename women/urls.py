from django.urls import path,re_path

from .views import *

urlpatterns = [
    path('', index, name = 'home'),#именуется параметр name для редиректа 301/302
    path('about/',about, name = 'about' )
]

