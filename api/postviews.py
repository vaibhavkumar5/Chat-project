from django.urls import path
from django.shortcuts import render

from rest_framework.decorators import api_view

from .postserializers import *

from utility.apiresponse import ApiResponse

@api_view(['GET'])
def GetPost(request, postid):
	serializer = GetPostSerializer
	queryset = Post.objects.get(PostId = postid)
	return ApiResponse(queryset, serializer, False)

@api_view(['GET'])
def GetPosts(request):
	serializer = GetPostSerializer
	queryset = Post.objects.all()
	return ApiResponse(queryset, serializer)