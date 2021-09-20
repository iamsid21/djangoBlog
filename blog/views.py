from django.shortcuts import render

# Create your views here.
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request,'blog/index.html',{'posts':posts})