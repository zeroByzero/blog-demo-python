from django.shortcuts import render, render_to_response, get_object_or_404
from blogpost.models import Blogpost

# Create your views here.


def index(request):
    print("hello world")
    return render_to_response('index.html', {
        'post': Blogpost.objects.all()[:5]
    })


def view_post(request, slug):
    return render_to_response('blogpost_detail.html', {'post': get_object_or_404(Blogpost, slug=slug)})
