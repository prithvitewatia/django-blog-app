from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile


class UserSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar', False)

        if avatar:
            if avatar.size > 1 * 1024 * 1024:
                raise forms.ValidationError('Avatar size should be less than 1MB.')

            valid_mime_types = ['image/jpeg', 'image/png']

            if hasattr(avatar, 'content_type') and avatar.content_type not in valid_mime_types:
                raise forms.ValidationError('Invalid file type, only jpeg or png are allowed')

        return avatar


