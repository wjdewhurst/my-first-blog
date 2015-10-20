from django.shortcuts import render
from django.utils import timezone
# Dot before 'models' means current directory/application
from .models import Post


# Function called 'post_list', takes request, returns function 'render' to render template.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    return render(request, 'blog/post_list.html', {"posts": posts})
