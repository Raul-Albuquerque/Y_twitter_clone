from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from ..forms import SignUpForm

def signup(request):
  form = SignUpForm()
  return render(request, 'signup.html', {'form':form})

def feed(request):
  form = SignUpForm(request.POST)
  if form.is_valid():
    username = form.cleaned_data['usuario']
    first_name = form.cleaned_data['nome'].lower()
    last_name = form.cleaned_data['sobrenome'].lower()
    email = form.cleaned_data['email'].lower()
    password_1 = form.cleaned_data['senha_1']
    password_2 = form.cleaned_data['senha_2']
    return HttpResponse(f'Usuário={username}, nome={first_name}, sobrenome={last_name}, email={email}, senha={password_1}, senha2={password_2}')
  else:
    return HttpResponse('deu errado')
