from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages


#  views here.
def index(request):
    """Return the index.html file"""
    return render(request, 'index.html')


def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have sucessfully logged out! Hope to see back soon")
    return redirect(reverse('index'))
