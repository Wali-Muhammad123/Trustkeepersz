from rest_framework import serializers
from .models import Contact,BookMeeting

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'
class BookMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookMeeting
        fields='__all__'
        validators=[
            serializers.UniqueTogetherValidator(
                queryset=BookMeeting.objects.all(),
                fields=['email','phone']
            )
        ]