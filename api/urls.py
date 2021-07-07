from django.urls import path
from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .postviews import *
from .messageviews import *

@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'Api Overview':'',
		'Get All Posts':'getposts/',
		'Get Specific Post by Post ID':'getpost/postid/',
		'Make a New Post':'newpost/'
	}
	return Response(api_urls)

urlpatterns = [
	path('', ApiOverview),

	path('getposts', GetPosts),
	path('getpost/<str:postid>/', GetPost),

	path('newpost/', NewPost)

]