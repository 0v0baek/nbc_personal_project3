from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Q

from .models import Todo
from .serializers import TodoListSerializer, TodoCreateSerializer, TodoSerializer

# Todo 목록 (내 Todo만 보임)
class TodoView(APIView):
    def get(self, request):
        todos = Todo.objects.filter(user_id=request.user.id)
        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TodoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Todo detail
class TodoDetailView(APIView):
    def get(self, request, todo_id):
        todo = get_object_or_404(Todo, id=todo_id)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, todo_id):
        todo = get_object_or_404(Todo, id=todo_id)
        # 로그인 한 유저와 todo 작성 유저가 일치하는 지
        if request.user == todo.user:
            serializer = TodoCreateSerializer(todo, data=request.data)
            if serializer.is_valid():
                # todo를 완수하지 않았을 때
                if todo.is_complete == False:
                    serializer.save(completion_at = '')
                # todo를 완수했을 때
                else:
                    print(timezone.now())
                    serializer.save(completion_at = timezone.now())
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("권한이 없습니다!!!", status=status.HTTP_403_FORBIDDEN)


    def delete(self, request, todo_id):
        todo = get_object_or_404(Todo, id=todo_id)
        if request.user == todo.user:
            todo.delete()
            return Response("삭제 완료!", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다!!!", status=status.HTTP_403_FORBIDDEN)
        