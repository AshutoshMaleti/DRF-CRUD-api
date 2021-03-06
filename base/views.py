from django.http.response import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import TasksSerializer
from .models import Tasks

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
        }

    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks=Tasks.objects.all()
    serializer=TasksSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detailedView(request, pk):
    tasks=Tasks.objects.get(id=pk)
    serializer=TasksSerializer(tasks,many=False)
    return Response(serializer.data)

#create a new entry
@api_view(['POST'])
def create(request):
    serializer=TasksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

#update a pre written entry
@api_view(['POST'])
def update(request, pk):
    task=Tasks.objects.get(id=pk)
    serializer=TasksSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request, pk):
    task=Tasks.objects.get(id=pk)
    task.delete()

    return HttpResponse('data selection deleted')