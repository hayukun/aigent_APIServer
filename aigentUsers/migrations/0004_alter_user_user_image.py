# Generated by Django 4.2.2 on 2023-06-09 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aigentUsers', '0003_user_userid_user_user_bondname_user_user_hashcode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.ImageField(null=True, unique=True, upload_to='users_images/%Y%m_users/<django.db.models.fields.AutoField>.jpg'),
        ),
    ]
