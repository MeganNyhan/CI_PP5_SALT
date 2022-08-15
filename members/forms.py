from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


# Sign up form


class SignUpForm(UserCreationForm):
    """
        Sign up form
    """
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                             'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
                                 'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
                                'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',
                  'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


# edit profile form


class EditProfileForm(UserChangeForm):
    """
        Edit Profile Form
    """
    email = forms.EmailField(widget=forms.EmailInput
                             (attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput
                                 (attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput
                                (attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput
                               (attrs={'class': 'form-control'}))
    last_login = forms.CharField(max_length=100, widget=forms.TextInput
                                 (attrs={'class': 'form-control'}))
    is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput
                                   (attrs={'class': 'form-check'}))
    is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput
                                (attrs={'class': 'form-check'}))
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput
                                  (attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',
                  'last_login', 'is_active', 'is_superuser', 'date_joined')



# user profile form


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', )

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes to fields in profile form """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_email': 'Email',
            'default_phone_number': 'Phone Number',
            'default_country': 'Country',
            'default_postcode': 'Postcode',
            'default_town_or_city': 'Town Or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = '{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black profile-form-input'
            self.fields[field].label = False