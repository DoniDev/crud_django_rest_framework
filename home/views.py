from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from home.models import Task
from . serializers import TaskSerializer

@api_view(['GET'])
def home(request):

    api_url = {
        'List':'/task/list/',
        'Detail':'task/detail/<str:pk>',
        'Create':'/task/create/',
        'Update':'/task/update/',
        'Delete':'/task/delete',

    }

    return Response(api_url)


@api_view(['GET'])
def tasklist(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskdetail(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskcreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskupdate(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(data=request.data,instance=task)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskdelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Item succesfully deleted')





