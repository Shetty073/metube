from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from metube.decorators import signout_required

@signout_required()
def signin_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('videos'))  # Redirect to a 'home' view after successful login
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'identity/signin.html')
