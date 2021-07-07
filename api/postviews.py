from django.urls import path
from django.shortcuts import render
from django.http import Http404

from rest_framework.decorators import api_view

from .postserializers import *

from utility.apiresponse import *

@api_view(['GET'])
def GetPost(request, postid):
	serializer = GetPostSerializer
	if request.user.is_authenticated:
		try:
			queryset = Post.objects.get(PostId = postid)
		except:
			raise Http404(f"Post with id={postid} Does Not Exist")
		return ApiGetResponse(queryset, serializer, False)
	else:
		queryset = []
		return ApiGetResponse(queryset, serializer)

@api_view(['GET'])
def GetPosts(request):
	serializer = GetPostSerializer
	if request.user.is_authenticated:
		queryset = Post.objects.all()
	else:
		queryset = []
	return ApiGetResponse(queryset, serializer)

@api_view(['GET', 'POST'])
def NewPost(request):
	serializer = NewPostSerializer
	if request.method == 'POST' and request.user == User.objects.get(username=request.data['ByUser']):
		return ApiPostResponse(request, serializer)
	else:
		queryset = []
		return ApiGetResponse(queryset, serializer)