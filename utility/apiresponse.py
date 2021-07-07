from rest_framework.response import Response

def ApiGetResponse(queryset, serializer, many=True):
	serializer = serializer(queryset, many=many)
	return Response(serializer.data)

def ApiPostResponse(request, serializer):
	serializer = serializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)