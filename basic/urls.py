from django.urls import path,include
from . import views

urlpatterns = [  
    path('',views.base,name='base'),
    path('basic/create',views.create,name='create'),
    path('basic/read',views.read,name='read'),
    path('basic/<id_no>/userdetails',views.userdetails,name='userdetails'),
    path('basic/<id_no>/update',views.update,name='update'),
    path('basic/<id_no>/delete',views.delete,name='delete'),
]
