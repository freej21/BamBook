from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import *
from django.conf import settings
import sweetify
import random as r
import smtplib
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import *


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Log In Successfully.', extra_tags='success-auto-dismiss')
            # Redirect to the desired page after successful login

            if user.is_superuser:
                return redirect('visitors')  # Redirect to the admin dashboard
            
        else:
            messages.error(request, 'Incorrect username or password. Please try again.', extra_tags='error-auto-dismiss')
    else:
        form = LoginForm(request)
    return render(request, 'user/login.html', {'form': form, 'title': 'login'})


def logout_view(request):
    logout(request)
    # Redirect to the desired page after logout
    return redirect('add-visitor')