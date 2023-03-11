from django.shortcuts import render, redirect
from . models import Todo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import TodoSerializer
from rest_framework import status

@api_view(['GET'])
def tasks_view(request):
    if request.method == 'GET':
        todos = Todo.objects.all()

        serializer = TodoSerializer(todos, many = True)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def task_delete(request, pk):
    todo = Todo.objects.get(pk=pk)

    if request.method == 'DELETE':
        todo.delete()
        # return redirect('todo_views')
        return Response(status=status.HTTP_410_GONE)

@api_view(['POST'])
def task_create(request):
    if request.method == 'POST':
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
    # task = request.POST['task']
    # new_task = Todo(task=task)
    # new_task.save()
    # return Response(status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def task_edit(request, pk):
    task = Todo.objects.get(pk=pk)

    if request.method == 'PUT':
        serializer = TodoSerializer(task, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)