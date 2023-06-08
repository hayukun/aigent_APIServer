from rest_framework import serializers
from .models import User

# 参考
# https://chigusa-web.com/blog/django-rest-framework/
class UserSerializer(serializers.ModelSerializer):

    user_displayName = serializers.CharField(
        max_length=50,
        required=True
    )

    def rename_imageName(self, value):

        return value


    def validation_user_displayName(self, value):
        
        return value

    class Meta:
        model = User
        fields = ['user_displayName', 'user_image']
        read_only_fields = ['id', 'created_at', 'updated_at']

        
        
