from typing import ValuesView
from django.urls import path
from . import views



urlpatterns = [
    path('',views.getRouts, name='routs'),
    path('notes/',views.getNotes, name='notes'),
    path('notes/create',views.createNote, name="create-note"),
    path('notes/<str:pk>/update',views.updateNotes, name='update-note'),
    path('notes/<str:pk>/delete',views.deleteNote, name='delete-note'),
    path('notes/<str:pk>',views.getNote, name='note'),


]
