from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserDummyApiView, responseUserInfo

router = DefaultRouter()
router.register('userinfo', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dummy/', UserDummyApiView.as_view()),
    path('searchFriendInfo/', responseUserInfo),
]