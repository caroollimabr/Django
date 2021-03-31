from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:  # clique em inspecionar no input e cheque o name
            try:
                # Criar um novo usuario: 
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1']) 
                user.save()
                login(request, user)
                return redirect('currenttodos')

            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error': 'Username has already been taken - Choose a new one'})
        else:
            return render(request, 'todo/signupuser.html', 'form':UserCreationForm(), 'error': 'Passwords did not match')

def currenttodos(request):
    return render(request, 'todo/currenttodos.html')


