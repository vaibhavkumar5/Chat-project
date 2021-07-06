from rest_framework import serializers

from database.models import Message, StarredMessage

class GetMessageSerializer(serializers.ModelSerializer):
	class Meta(object):
		model = Message
		fields = (
				'__all__'
			)

class GetStarredMessageSerializer(serializers.ModelSerializer):
	class Meta(object):
		model = StarredMessage
		fields = (
				'__all__'
			)