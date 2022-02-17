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

from django.http import Http404
from rest_framework.views import APIView

# class APIView

class notes_list3(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        notes = Notes.objects.all()
        serializer = NotesSerializer1(notes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NotesSerializer1(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

class notes_detail3(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Notes.objects.get(pk=pk)
        except Notes.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        notes = self.get_object(pk)
        serializer = NotesSerializer1(notes)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        notes = self.get_object(pk)
        serializer = NotesSerializer1(notes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        


from rest_framework import mixins
from rest_framework import generics

# GenericAPIView + Mixins

class notes_list4(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                  
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer1

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class notes_detail4(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer1

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Concrete view classes

class SnippetList3(generics.ListCreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer1


class SnippetDetail3(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer1        

