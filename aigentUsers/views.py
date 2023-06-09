from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

# Create your views here.
# API画面でデータを確認できるクラス
class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.all() #filter(user_displayName='条件')
    serializer_class = UserSerializer

# ダミーデータを返すクラス
class UserDummyApiView(APIView):

    def get(self, request, format=None):

        return Response({"username", "http://localhost:8000/media/maxresdefault.jpg"})
    
@api_view(['GET'])
def responseUserInfo(request):

    if request.method == 'GET':
        if "user_displayName" in request.GET:
            getUser_displayName = request.GET.get(key="user_displayName")
        else:
            print("ELSE: not exist user_displayName")
            return Response(None)
        
        if "user_hashCode" in request.GET:
            getUser_hashCode = request.GET.get(key="user_hashCode")
        else:
            print("ELSE: not exist user_hashCode")
            return Response(None)

        bondName = getUser_displayName + '#' + getUser_hashCode

        try:
            user_info = User.objects.filter(user_bondName=bondName).all()
            #user_info = User.objects.all()
            serializer = UserSerializer(user_info, many=True)
        
            return Response(serializer.data)
        except:
            return Response(None)

