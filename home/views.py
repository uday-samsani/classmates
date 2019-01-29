from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .models import Post
from .forms import PostCreationForm


@login_required
def index(request):
    feed = Post.objects.filter(user=True)
    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            form.user.set(request.user)
            form.save()
            return redirect('/')
    else:
        form = PostCreationForm()
    return render(request, template_name='home/index.html', context={'name': request.user.first_name, 'form': form,
                                                                     'feed': feed})


@login_required
def createPost(request):
    return render(request, template_name='home/index.html', context={'name': request.user.first_name})
