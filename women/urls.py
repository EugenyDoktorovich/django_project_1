from django.urls import path,re_path

from .views import *

urlpatterns = [
    path('', index, name = 'home'),#именуется параметр name для редиректа 301/302
    path('about/',about, name = 'about' ),
    path('addpage/',addpage, name= 'addpage'),
    path('contact/',contact, name= 'contact'),
    path('login/',login, name= 'login'),
    path('post/<int:post_id>/', show_post, name ='post')#post_id - pk связка

]

