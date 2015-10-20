from django.shortcuts import render


# Function called 'post_list', takes request, returns function 'render' to render template.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
