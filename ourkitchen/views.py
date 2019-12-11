from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_exempt


def index(request):
    if request.user.is_authenticated:   # 인증된 유저가 요청을 보낸 경우, 로그인 페이지를 보여주지 않고 목록 페이지로 redirect
        return render(request, 'index.html')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('index')
    else:
        form = AuthenticationForm()
        return render(request, 'index.html', {'form':form})