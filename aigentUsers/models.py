from django.db import models
import datetime

# Create your models here.

# ユーザの画像データリネームして保存先を指定する関数
def save_imagePath(instance, filename):
    now = datetime.datetime.now()
    ext = filename.split('.')[-1]
    new_name = 'users_images/' + now.strftime("%Y_%m_%d") + '/' + instance.user_bondName
    return f'{new_name}.{ext}'


# ユーザ情報格納テーブル
class User(models.Model):

    id = models.AutoField(primary_key=True)
    user_bondName = models.CharField(unique=True, max_length=210, default=None)
    user_displayName = models.CharField(max_length=200)
    user_hashCode = models.IntegerField(default=0000)
    # LINE user ID
    userId = models.CharField(unique=True, max_length=50, default=None)
    pictureUrl = models.ImageField(upload_to=save_imagePath, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_displayName

    