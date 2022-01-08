from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")
    
def chatroom(request):
    return render(request, "chatroom.html")
