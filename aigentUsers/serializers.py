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

    userID = serializers.CharField(
        max_length=50,
    )

    user_hashCode = serializers.IntegerField(
        required=True
    )



    # def validation_user_displayName(self, value):
        
    #     return value

    class Meta:
        model = User
        fields = ['user_displayName', 'user_hashCode', 'userID', 'user_image']
        read_only_fields = ['id', 'user_bondName', 'created_at', 'updated_at']

        
        
