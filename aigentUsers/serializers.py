from rest_framework import serializers
from .models import User

# 参考
# https://chigusa-web.com/blog/django-rest-framework/
class UserSerializer(serializers.ModelSerializer):
    # ここに記載したものはfieldに記載しないといけない
    user_displayName = serializers.CharField(
        max_length=200,
        required=True
    )

    userId = serializers.CharField(
        max_length=50,
    )

    user_hashCode = serializers.IntegerField(read_only=True)

    user_bondName = serializers.CharField(read_only=True)

    pictureUrl = serializers.ImageField()


    # def validation_user_displayName(self, value):
        
    #     return value

    class Meta:
        model = User
        fields = ['user_displayName', 'user_hashCode', 'user_bondName', 'userId', 'pictureUrl']
        read_only_fields = ['id', 'created_at', 'updated_at']

        
        
