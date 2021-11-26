from django.http import response
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .seriliazers import NoteSerializer

# Create your views here.

@api_view(['GET'])
def getRouts(request):
  return Response('our Api')


@api_view(['GET'])
def getNotes(request):
  notes=Note.objects.all().order_by('-updated')

  serializer=NoteSerializer(notes,many=True)

  return Response(serializer.data)




@api_view(['GET'])
def getNote(request,pk):
  notes=Note.objects.get(id=pk)

  serializer=NoteSerializer(notes,many=False)

  return Response(serializer.data)




@api_view(['POST'])
def createNote(request):
  data=request.data
  note=Note.objects.create(
    body=data['body']
  )

  serializer=NoteSerializer(note, many=False)


  return Response(serializer.data)








@api_view(['PUT']) #PUT request for update item
def updateNotes(request,pk):
  data=request.data
  note=Note.objects.get(id=pk)
  serializer=NoteSerializer(instance= note,data=data)

  if serializer.is_valid():
    serializer.save()


  return Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(request,pk):
  note=Note.objects.get(id=pk)
  note.delete()
  return Response('Note was deleted!')





