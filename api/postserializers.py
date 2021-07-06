from rest_framework import serializers

from database.models import Post, StarredPost

class GetPostSerializer(serializers.ModelSerializer):
	class Meta(object):
		model = Post
		fields = (
				'__all__'
			)

class GetStarredPostSerializer(serializers.ModelSerializer):
	class Meta(object):
		model = StarredPost
		fields = (
				'__all__'
			)