
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, PostTemplate
from .forms import PostForm, PostTemplateForm

def dashboard(request):
    posts = Post.objects.all()
    return render(request, 'scheduling/dashboard.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'scheduling/post_detail.html', {'post': post})

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # If no scheduled time is provided, use the current time
            if not post.scheduled_time:
                post.scheduled_time = timezone.now()
            post.save()
            return redirect('dashboard')
    else:
        form = PostForm()
    return render(request, 'scheduling/create_post.html', {'form': form})

def manage_templates(request):
    templates = PostTemplate.objects.all()
    return render(request, 'scheduling/manage_templates.html', {'templates': templates})

def create_template(request):
    if request.method == "POST":
        form = PostTemplateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_templates')
    else:
        form = PostTemplateForm()
    return render(request, 'scheduling/create_template.html', {'form': form})





