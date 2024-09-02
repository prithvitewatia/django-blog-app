from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import UserSignupForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


# Create your views here.
class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'registration/signup.html'
    form_class = UserSignupForm
    success_url = reverse_lazy('users:login')
    success_message = '%(username) You have been successfully registered!'


class ProfileView(UpdateView):
    model = Profile
    template_name = 'users/profile.html'
    def get(self, request, *args, **kwargs):
        user = request.user
        user_update_form = UserUpdateForm(instance=user)
        profile_update_form = ProfileUpdateForm(instance=user.profile)
        if user.is_authenticated:
            return render(request, self.template_name, {
                "u_form": user_update_form,
                "p_form": profile_update_form,
                "user": user
            })
        else:
            return redirect('users:login')

    def post(self, request, *args, **kwargs):
        user = request.user
        user_update_form = UserUpdateForm(request.POST, instance=user)
        profile_update_form = ProfileUpdateForm(request.POST, instance=user.profile)
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, 'Profile Updated Successfully!')
            return redirect('users:profile')
        else:
            return render(request, self.template_name, {
                "u_form": user_update_form,
                "p_form": profile_update_form,
                "user": user
            })

