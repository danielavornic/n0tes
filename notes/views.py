from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import NoteForm
from .models import Note

def home(request):
    if request.user.is_authenticated:
        return redirect('all_notes')
    else:
        return render(request, 'notes/home.html')

def signup_user(request):
    if request.user.is_authenticated:
        return redirect('all_notes')
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
                    return redirect('all_notes')
                except IntegrityError:
                    return render(request, 'notes/signupuser.html', {'form': UserCreationForm(), 'error': 'That username has already been taken'})
            else:
                return render(request, 'notes/signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})

def login_user(request):
    if request.user.is_authenticated:
        return redirect('all_notes')
    else:
        if request.method == "GET":
            return render(request, 'notes/loginuser.html', {'form': AuthenticationForm()})
        else:
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is None:
                return render(request, 'notes/loginuser.html', {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
            else:
                login(request, user)
                return redirect('all_notes')

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    
def add_note(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, 'notes/addnote.html', {'note': 'true', 'form': NoteForm()})
        else:
            form = NoteForm(request.POST)
            note = form.save(commit=False)
            note.user = request.user
            if not note.title:
                note.title = 'Untitled'
            note.save()
            return render(request, 'notes/note.html', {'note': note, 'form': form})
    else:
        return redirect('home')

def all_notes(request):
    if request.user.is_authenticated:
        usernotes = Note.objects.filter(user=request.user, archive=False).order_by('-date')
        active = 'noteLink'
        return render(request, 'notes/notes.html', {'notes': usernotes, 'active': active})
    else:
        return redirect('home')

def important_notes(request):
    if request.user.is_authenticated:
        important = Note.objects.filter(user=request.user, important=True, archive=False).order_by('-date')
        active = 'importantLink'
        return render(request, 'notes/important.html', {'notes': important, 'active': active})
    else:
        return redirect('home')

def archive(request):
    if request.user.is_authenticated:
        archive = Note.objects.filter(user=request.user, archive=True).order_by('-date')
        active = 'archiveLink'
        return render(request, 'notes/archive.html', {'notes': archive, 'active': active})   
    else:
        return redirect('home')

def note(request, note_pk):
    if request.user.is_authenticated:
        note = get_object_or_404(Note, pk=note_pk, user=request.user)
        if request.method == "GET":
            form = NoteForm(instance=note)
            return render(request, 'notes/note.html', {'note': note, 'form': form})
        else:
            form = NoteForm(request.POST, instance=note)
            note = form.save(commit=False)
            if not note.title:
                note.title = 'Untitled'
            form.save()
            return render(request, 'notes/note.html', {'note': note, 'form': form})
    else:
        return redirect('home')

def delete_note(request, note_pk):
    note = get_object_or_404(Note, pk=note_pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('all_notes')

def archive_note(request, note_pk):
    note = get_object_or_404(Note, pk=note_pk, user=request.user)
    form = NoteForm(instance=note)
    if request.method == 'POST':
        note.archive = not note.archive
        note.save()
        return render(request, 'notes/note.html', {'note': note, 'form': form})

def search(request):
    if request.user.is_authenticated:
        active = 'searchLink'
        if request.method == "GET":
            keyword = request.GET.get('keyword', None);
            if keyword:
                notes = Note.objects.filter(title__icontains=keyword, user=request.user) | Note.objects.filter(text__icontains=keyword, user=request.user)
                return render(request, 'notes/search.html', {'notes': notes, 'keyword': keyword, 'active': active})  
        return render(request, 'notes/search.html', {'active': active}) 
    else:
        return redirect('home')

def delete_user(request):   
    if request.user.is_authenticated: 
        u = User.objects.get(username=request.user.username)
        u.delete()
    return redirect('home')

def profile(request):
    if request.user.is_authenticated:
        active = 'profileLink'
        notes_count = Note.objects.filter(user=request.user).count()
        return render(request, 'notes/profile.html', {'active': active, 'notes_count': notes_count})
    else:
        return redirect('home')