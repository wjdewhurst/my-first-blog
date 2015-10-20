from django.conf.urls import url

# Importing all views from Blog application
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
