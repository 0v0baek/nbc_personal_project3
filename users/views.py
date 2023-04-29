from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .models import User
from .serializers import UserSerializer, UserProfileSerializer, UserEditSerializer

# 유저 회원가입
class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입 완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)

# 유저 프로필
class UserProfileView(APIView):
    # 유처 프로필 확인
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
    
    # 유저 프로필 수정
    def put(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        # 프로필 유저와 현재 유저가 일치하는지 확인
        # headers에 Authorization, token 실어주기
        if request.user.id == user_id:
            serializer = UserEditSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("유저 정보가 일치하지 않습니다", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        # 프로필 유저와 현재 유저가 일치하는지 확인
        # headers에 Authorization, token 실어주기
        if request.user.id == user_id:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response("유저 정보가 일치하지 않습니다", status=status.HTTP_400_BAD_REQUEST)