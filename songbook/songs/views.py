from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Song

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'songs/index.html'
    context_object_name = 'songs'

    def get_queryset(self):
        return Song.objects.all()

class DetailView(generic.DetailView):
    model = Song
    template_name = 'songs/detail.html'
    

    def get_queryset(self):
        return Song.objects.all()
