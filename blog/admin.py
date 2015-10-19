from django.contrib import admin
from .models import Post

# Import and register created 'Post' model to make it viewable on the admin page.
admin.site.register(Post)