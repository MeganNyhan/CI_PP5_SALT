# Imports
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import BadHeaderError
from home.models import Profile
from .forms import SignUpForm, EditProfileForm, UserProfileForm
from .models import UserProfile
from checkout.models import Order


# user registration view


class UserRegisterView(generic.CreateView):
    """
        Login function
    """
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


# registration view


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


# user edit view


class UserEditView(generic.UpdateView):
    """ 
        Edit User Function
    """
    form_class = EditProfileForm
    template_name = 'registration/edit-profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


# show profile page view

    
class ShowProfilePageView(DetailView):
    """
        Show Profile View
    """
    model = Profile
    template_name = 'registration/user-profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args,
                                                                     **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context


# profile view


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Your edits were unsuccessfull. \
                Please try again.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'registration/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


# order history view


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, 'You are looking at a past order confirmation for order number: {order_number}.\
                  A confirmation email was sent on the date of order.')

    template = 'checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)