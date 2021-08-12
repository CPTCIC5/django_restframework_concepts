from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes #permission classes are set to restrict  user 
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from django.http import Http404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly  #to set permissions
from django.views.decorators.cache import cache_page # this is used to cache the page in django not only in rest framework
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle #it is used to throttle , throttle is a process to limit user to make no. of requests
from rest_framework import filters



@api_view(['GET'])
def test_prog(request):
    data={'Age':16,'Name':'Aryan'}
    return Response(data)


class TaskList(generics.ListAPIView):
    queryset= Task.objects.all()
    serializer_class= TaskSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes=[UserRateThrottle,AnonRateThrottle]
    filter_backends = [filters.OrderingFilter]
    search_fields= ['task']


'''
@api_view
@cache_page(60*60*2)
@permission_classes([IsAuthenticatedOrReadOnly])
def tasklist(request):
    qs=Task.objects.all()   
    serializer=TaskSerializer(qs,many=True)
    return Response(serializer.data)
'''

@api_view(['GET'])
@cache_page(60*60*2)
def taskdetail(request,question_id):
    try:
        tasks=Task.objects.get(id=question_id)
        serializer= TaskSerializer(tasks, many=False)
    except Task.DoesNotExist:
        raise Http404('OBJ NOT FOUND')
    return Response(serializer.data)


class TaskCreator(generics.CreateAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    permission_classes=[AllowAny]
    cache_page=(60*60*2)
    throttle_classes=[UserRateThrottle]

'''
@api_view(['POST'])
@cache_page(60*60*2)
@throttle_classes=[UserRateThrottle]
@permission_classes(['IsAuthenticatedOrReadOnly'])
def taskcreator(request):
    form=TaskSerializer(data=request.data)
    if form.is_valid():
        form.save()
        return Response(form.data)
    return Response(form.errors)
'''

@api_view(['PUT'])
def taskupdate(request,question_id):
    task=Task.objects.get(id=question_id)
    serialize=TaskSerializer(instance=task,data=request.data)
    if serialize.is_valid():
        serialize.save()
    return Response(serialize.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def taskdelete(request,question_id):
    try:
        task=Task.objects.get(id=question_id).delete()
    except Task.DoesNotExist:
        return Response("OBJ NOT EXISTS")
    return Response(f"TASK HAVE BEEN DELETED {task} ")  