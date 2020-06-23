from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import NoteForm

def home(request):
    if request.user.is_authenticated:
        return render(request, 'notes/notes.html')
    else:
        return render(request, 'notes/home.html')

def signupuser(request):
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

def notes(request):
    return render(request, 'notes/notes.html')

def addnote(request):
    if request.method == "GET":
        return render(request, 'notes/addnote.html', {'form': NoteForm()})
    else:
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            if not note.text and not note.title:
                return redirect('notes')
            else:
                note.save()
        return redirect('notes')        