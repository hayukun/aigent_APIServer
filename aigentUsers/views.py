from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Friend
from .serializers import UserSerializer
import random
import requests
import io
from django.core.files import File

# Create your views here.
# API画面でデータを確認できるクラス(いずれ消す)
class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.all() #filter(user_displayName='条件')
    serializer_class = UserSerializer

# ダミーデータを返すクラス(いずれ消す)
class UserDummyApiView(APIView):

    def get(self, request, format=None):

        return Response({"username", "http://localhost:8000/media/test_images/test0000.jpg"})

# ユーザーを検索するGETメソッド(主にフレンド検索で使用)    
@api_view(['GET'])
def responseUserInfo(request):

    if request.method == 'GET':
        if "user_displayName" in request.GET:
            getUser_displayName = request.GET.get(key="user_displayName")
        else:
            print("ELSE: not exist user_displayName")
            return Response({'error':'ユーザー名の取得に失敗しました[ERROR:01]'}, status=status.HTTP_400_BAD_REQUEST)
        
        if "user_hashCode" in request.GET:
            getUser_hashCode = request.GET.get(key="user_hashCode")
        else:
            print("ELSE: not exist user_hashCode")
            return Response({'error':'ハッシュコードの取得に失敗しました[ERROR:02]'}, status=status.HTTP_400_BAD_REQUEST)

        bond_name = getUser_displayName + '#' + getUser_hashCode

        try:
            user_info = User.objects.filter(user_bondName=bond_name).all()
            if user_info.exists():
                serializer = UserSerializer(user_info, many=True)
                return Response(serializer.data)
            else:     
                return Response({'error':'ユーザーの取得に失敗しました[ERROR:03]'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error':'ユーザーの取得に失敗しました[ERROR:04]'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
           return Response({'error':'ユーザーの取得に失敗しました[ERROR:05]'}, status=status.HTTP_400_BAD_REQUEST) 

# LINEサインインでサインインしたユーザをDBに登録するPOSTメソッド
@api_view(['POST'])
def registerUserInfo(request):
    data = request.data

    if not data.get('user_displayName'):
        return Response({'error':'ユーザー名の取得に失敗しました[ERROR:06]'}, status=status.HTTP_400_BAD_REQUEST)
    
    if not data.get('userId'):
        return Response({'error':'ユーザーIDの取得に失敗しました[ERROR:07]'}, status=status.HTTP_400_BAD_REQUEST)
    
    if not data.get('pictureUrl'):
        return Response({'error':'アイコン画像の取得に失敗しました[ERROR:08]'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            # LINE Picture URLから画像を取得する
            response = requests.get(data.get('pictureUrl'))
            response.raise_for_status()
            if response.status_code == 200: # 画像を取得できたかステータスコードで判定
                image_data = response.raw # rawで格納
        except requests.exceptions.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    bond_name = ''
    loopCount = 0
    
    while True:
        random_int = random.randint(1000, 9999)
        bond_name = data['user_displayName'] + f"#{random_int}"

        if not User.objects.filter(user_bondName=bond_name).exists():
    
            data['user_bondName'] = bond_name
            data['user_hashCode'] = random_int
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                new_user = serializer.save()
                new_user.pictureContent.save(f"{new_user.pictureUrl}", File(image_data))
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        
        if loopCount >= 100:
            return Response({'error':'ユーザーの登録に失敗しました[ERROR:09]'}, status=status.HTTP_400_BAD_REQUEST) 
        else:
            loopCount += 1

# フレンド登録するPOSTメソッド
@api_view(['POST'])
def add_Newfriend(request):
    getUser_bondName = request.data.get('user_bondName')
    getFriend_bondName = request.data.get('friend_bondName')

    try:
        user = User.objects.get(user_bondName=getUser_bondName)
        friend = User.objects.get(user_bondName=getFriend_bondName)

        if user == friend:
            return Response({'error':'自身をフレンド追加することはできません。'}, status=status.HTTP_400_BAD_REQUEST)
        
        friend_obj, created = Friend.objects.get_or_create(user=user, friend=friend)

        if created:
            return Response({'message': friend.user_bondName + 'さんをフレンドを登録しました。'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': friend.user_bondName + 'さんはすでにフレンドです。'}, status=status.HTTP_200_OK)
        
    except User.DoesNotExist:
        return Response({'error':'ユーザーが存在しません。[ERROR:10]'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)