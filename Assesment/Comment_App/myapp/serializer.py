from rest_framework import serializers

from myapp.models import CommentData


class commentSerial(serializers.ModelSerializer):
    class Meta:
        model=CommentData
        fields='__all__'
