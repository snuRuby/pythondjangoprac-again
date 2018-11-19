from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from bookmark.models import Bookmark

class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model=Bookmark                                                                                                                                                                                                                                                                                                                                              

# Create your views here.
