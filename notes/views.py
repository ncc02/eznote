from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def index(request):
    list_note = Note.objects.filter(private=False).order_by("-create_at")
    context = {
        "list_note" : list_note,
    }
    return render(request, "notes/index.html", context)

from django.http import HttpResponse

def detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if note.private:
        return HttpResponse("This is a private note")
    return render(request, "notes/detail.html", {"note": note})