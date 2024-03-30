from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from ..forms import SignUpForm

def signup(request):
  form = SignUpForm()
  if request.method == 'GET':
      return render(request, 'signup.html', {'form':form})
  else:
    form = SignUpForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['usuario']
      first_name = form.cleaned_data['nome'].lower()
      last_name = form.cleaned_data['sobrenome'].lower()
      email = form.cleaned_data['email']
      password = form.cleaned_data['senha']

      double_user = User.objects.filter(username=username).first()

      if double_user:
        return HttpResponse('Usuário já existe')   
      else:
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
        user.save()
        # user.authenticate(username=username, password=password)
        login(request,username=username, password=password)
        return redirect('feed_tweets')
    else:
      return HttpResponse('Algo deu errado')