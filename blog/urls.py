from django.conf.urls import url

# Importing all views from Blog application
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	# (?<pk>[0-9]+) = Everything here will be transferred to a variable called 'pk'.
	# [0-9] = Must be a number.
	# + = Must be one or more digits.
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]
