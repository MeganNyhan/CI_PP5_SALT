# Imports
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import BadHeaderError
from .forms import SignUpForm


class UserRegisterView(generic.CreateView):
    """
        Login function
    """
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


def register(request):
    """
        Validation in form
    """
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                return redirect('/')
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            messages.success(request, 'You have Successfully registered')
            return redirect('login.html')
        messages.error(request, "Error. Account not created please try again.")

        form = SignUpForm()
    return render(request, 'base.html', {'form': form})
