from django.shortcuts import render, redirect
from .forms import NoteForm


def generate_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/admin")
    else:
        form = NoteForm()
    return render(request, "add_note.html", {"form": form})
