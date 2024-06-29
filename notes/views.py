from . import models
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView
from django.views.generic.edit import DeleteView 
from django.contrib.auth.mixins import LoginRequiredMixin
from  . import forms
from django.http import HttpResponseRedirect

class NotesSuccessTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'notes/success200ok.html'
    login_url = '/login/'  

class NotesCreateView(LoginRequiredMixin, CreateView):
    model = models.Note
    form_class = forms.NotesForm
    success_url = '/smart/notes/new/success'
    login_url = '/login/'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Note
    form_class = forms.NotesForm
    success_url = '/smart/notes/new/success'
    login_url = '/login/'
    
class NotesListView(LoginRequiredMixin, ListView):
    model = models.Note
    context_object_name = "notes"
    login_url = '/login/'
    template_name = 'notes/notes_list.html'

class NotesDetailView(LoginRequiredMixin, DetailView):
    model = models.Note
    context_object_name = 'note'
    template_name = 'notes/note_details.html'
    login_url = '/login/'
    
    def get_queryset(self):
        return self.request.user.notes.all()
    
    
class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Note
    template_name = 'notes/note_delete.html'
    success_url = '/smart/notes/new/success'
    login_url = '/login/'