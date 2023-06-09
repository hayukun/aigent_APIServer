from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
import random
import requests

# Create your views here.
# API画面でデータを確認できるクラス
class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.all() #filter(user_displayName='条件')
    serializer_class = UserSerializer

# ダミーデータを返すクラス
class UserDummyApiView(APIView):

    def get(self, request, format=None):

        return Response({"username", "http://localhost:8000/media/test_images/test0000.jpg"})
    
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

        bond_name = getUser_displayName + '#' + getUser_hashCode

        #try:
        user_info = User.objects.filter(user_bondName=bond_name).all()
        #user_info = User.objects.all()
        serializer = UserSerializer(user_info, many=True)
    
        return Response(serializer.data)
        #except:
        #    return Response(None)

@api_view(['POST'])
def registerUserInfo(request):
    data = request.data

    if not data.get('user_displayName'):
        return Response({'error':'ユーザー名の取得に失敗しました'}, status=status.HTTP_400_BAD_REQUEST)
    
    if not data.get('userId'):
        return Response({'error':'ユーザーIDの取得に失敗しました'}, status=status.HTTP_400_BAD_REQUEST)
    
    if not data.get('pictureUrl'):
        return Response({'error':'アイコン画像の取得に失敗しました'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        response = requests.get(data.get('pictureUrl'))
        if response.status_code == 200:
            data['pictureUrl'] = response.content

    bond_name = ''
    
    while True:
        random_int = random.randint(1000, 9999)
        bond_name = data['user_displayName'] + f"#{random_int}"

        if not User.objects.filter(user_bondName=bond_name).exists():
    
            data['user_bondName'] = bond_name
            data['user_hashCode'] = random_int
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
