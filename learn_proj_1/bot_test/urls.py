from django.urls import path

from .views import chatroom,index,description

urlpatterns=[
    path('',index,name='index'),
    path('chat',chatroom,name='chatroom'),
    path('description',description,name='description')
]