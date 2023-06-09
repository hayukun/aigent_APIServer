from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    # ここに記載したものはfieldに記載しないといけない
    user_displayName = serializers.CharField(
        max_length=200,
        required=True
    )

    userId = serializers.CharField(
        max_length=50,
    )

    class Meta:
        model = User
        fields = ['user_displayName', 'user_hashCode', 'user_bondName', 'userId', 'pictureContent', 'pictureUrl']
        read_only_fields = ['id', 'created_at', 'updated_at']

        
        
