from . import views
from django.urls import path

urlpatterns = [
    path("notes/", views.NotesListView.as_view(), name='notes.list'),
    path("notes/new", views.NotesCreateView.as_view(), name='notes.new'),
    path("notes/new/success", views.NotesSuccessTemplateView.as_view(), name='notes.new.success'),
    path("notes/<pk>", views.NotesDetailView.as_view(), name='note.details'),
    path("notes/<pk>/edit", views.NotesUpdateView.as_view(), name='notes.update'),
    path("notes/<pk>/delete", views.NotesDeleteView.as_view(), name='notes.delete'),
]
