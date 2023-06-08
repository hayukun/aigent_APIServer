from django.db import models

# Create your models here.

# # ユーザの画像データ格納テーブル
# class Image(models.Model):

#     id = models.AutoField(primary_key=True)
#     #image_type = models.CharField(max_length=64)
#     image_content = models.BinaryField(null=True)
#     #image_size = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.id

# ユーザ情報格納テーブル
class User(models.Model):

    id = models.AutoField(primary_key=True)
    user_displayName = models.CharField(unique=True, max_length=200)
    user_image = models.ImageField(upload_to='users_images/%Y%m_users/', null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_displayName

    