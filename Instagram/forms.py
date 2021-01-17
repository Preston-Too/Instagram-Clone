from django import forms
from django.contrib.auth.models import User
from .models import Image, Profile, Comment
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

    def save(self, commit=True):
        user=super().save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['prof_pic', 'bio']

class ImageUploadForm(forms.ModelForm):
    image = forms.ImageField(label = "Image:")
    name = forms.CharField(label = "Image Name:", max_length=50)
    caption = forms.CharField(label = "Image Caption:", max_length=300)