from rest_framework.response import Response

def ApiResponse(queryset, serializer, many=True):
	serializer = serializer(queryset, many=many)
	return Response(serializer.data)