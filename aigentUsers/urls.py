from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserDummyApiView, responseUserInfo, registerUserInfo, add_Newfriend

router = DefaultRouter()
router.register('userinfo', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dummy/', UserDummyApiView.as_view()),
    
    path('searchFriendInfo/', responseUserInfo), # ユーザー検索
    path('register/', registerUserInfo), # 新規ユーザー登録
    path('addFriend/', add_Newfriend)  # フレンド追加
]