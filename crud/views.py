from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, DetailView
from django.contrib import messages



class IndexView(ListView):
    template_name = 'crud/index.html'
    model = Post
    post_list = Post.objects.all()
    context_object_name = 'post_list'


class PostDetailView(DetailView):
    model = Post
    template_name = 'crud/post-detail.html'


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = PostForm()
    context = {
        'form':form
    }
    return render(request, 'crud/create-post.html',context)


def post_edit(request,pk):
    post = get_object_or_404(Post,pk=pk)
    form = PostForm(request.POST or None,instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')    
    context = {
        'form':form
    }
    return render(request, 'crud/edit-post.html',context)



def post_delete(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post successfully deleted!")
        return redirect('index')
    context = {
        'object':post
    } 
    return render(request,'crud/delete.html',context)    

    
