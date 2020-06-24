from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import NoteForm
from .models import Note

def home(request):
    if request.user.is_authenticated:
        return redirect('notes')
    else:
        return render(request, 'notes/home.html')

def signupuser(request):
    if request.user.is_authenticated:
        return redirect('notes')
    else:
        if request.method == "GET":
            return render(request, 'notes/signupuser.html', {'form': UserCreationForm()})
        else:
            if len(request.POST['password1']) < 8:
                    return render(request, 'notes/signupuser.html', {'form': UserCreationForm(), 'error': 'Your password must contain at least 8 characters'})
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                    user.save()
                    login(request, user)
                    return redirect('notes')
                except IntegrityError:
                    return render(request, 'notes/signupuser.html', {'form': UserCreationForm(), 'error': 'That username has already been taken'})
            else:
                return render(request, 'notes/signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})

def loginuser(request):
    if request.user.is_authenticated:
        return redirect('notes')
    else:
        if request.method == "GET":
            return render(request, 'notes/loginuser.html', {'form': AuthenticationForm()})
        else:
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is None:
                return render(request, 'notes/loginuser.html', {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
            else:
                login(request, user)
                return redirect('notes')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    
def add(request):
    if request.method == "GET":
        return render(request, 'notes/addnote.html', {'form': NoteForm()})
    else:
        form = NoteForm(request.POST)
        note = form.save(commit=False)
        note.user = request.user
        if not note.title:
            note.title = 'New note'
        note.save() 
        return redirect('notes')   

def notes(request):
    usernotes = Note.objects.filter(user=request.user, archive=False).order_by('-date')
    return render(request, 'notes/notes.html', {'notes': usernotes})

def important(request):
    important = Note.objects.filter(user=request.user, important=True).order_by('-date')
    return render(request, 'notes/important.html', {'important': important})

def showarchive(request):
    archive = Note.objects.filter(user=request.user, archive=True).order_by('-date')
    return render(request, 'notes/archive.html', {'archive': archive})   

def note(request, note_pk):
    note = get_object_or_404(Note, pk=note_pk, user=request.user)
    if request.method == "GET":
        form = NoteForm(instance=note)
        return render(request, 'notes/note.html', {'note': note, 'form': form})  
    else:
        form = NoteForm(request.POST, instance=note)
        note = form.save()
        if not note.title:
            note.title = 'New note'
        form.save()
    return redirect('notes')

def delete(request, note_pk):
    note = get_object_or_404(Note, pk=note_pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('notes')

def archive(request, note_pk):
    note = get_object_or_404(Note, pk=note_pk, user=request.user)
    if request.method == 'POST':
        note.archive = not note.archive
        note.save()
        if note.archive:
            return redirect('showarchive')
        else:
            return redirect('notes')

def search(request):
    if request.method == "GET":
        keyword = request.GET.get('keyword', None);
        if keyword:
            notes = Note.objects.filter(title__icontains=keyword) | Note.objects.filter(text__icontains=keyword)
            return render(request, 'notes/search.html', {'notes': notes, 'keyword': keyword})  
    return render(request, 'notes/search.html') 