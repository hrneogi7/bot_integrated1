from django.urls import path

from .views import chatroom,index

urlpatterns=[
    path('',index,name='index'),
    path('chat',chatroom,name='chatroom')
]