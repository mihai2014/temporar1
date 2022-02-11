from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from notes.models import Notes
from notes.api.serializers import NotesSerializer1

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

# regular Django views (return JsonResponse)

# no csrf !
@csrf_exempt
#@csrf_protect
def notes_list1(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        notes = Notes.objects.all()
        serializer = NotesSerializer1(notes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NotesSerializer1(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def notes_detail1(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = NotesSerializer1(note)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = NotesSerializer1(note, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        note.delete()
        return HttpResponse(status=204) 


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# decorator (return Api Response)

@api_view(['GET', 'POST'])
def notes_list2(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        notes = Notes.objects.all()
        serializer = NotesSerializer1(notes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NotesSerializer1(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)             

@api_view(['GET', 'PUT', 'DELETE'])
def notes_detail2(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NotesSerializer1(note)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = NotesSerializer1(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        
