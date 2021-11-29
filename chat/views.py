from django.contrib.auth import authenticate, login, logout, hashers
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import User

from chat.forms import SignUpForm, AuthForm
from .serializers import GroupChatListSerializer, MessagesSerializer
from .models import GroupChat


def home(request):
    return render(request, 'base.html')

@login_required(login_url='/chat/login/')
def chat(request):
    return render(request, 'chat/index.html')

@login_required(login_url='/chat/login/')
def room(request, room_name):
    groups = GroupChat.objects.get(name=room_name)
    if not groups:
        return redirect('/chat')
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

def logout(request):
    logout(request)
    return redirect('/chat')

def log_in(request):
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('/chat')
    else:
        form = AuthForm()
    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = User.objects.filter(username=username).first()
            if not user:
                hashed_pass = hashers.make_password(raw_password)
                user = User.objects.create(username=username, password=hashed_pass)
                user.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/chat')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# Create your views here.
