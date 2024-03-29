from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from blog.models import Post, Profile

from blog.models import Profile
from .forms import SignUpForm, EditProfileForm, PasswordChangeForm, ProfilePageForm, EditProfilePageForm

class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    # fields = '__all__'
    template_name = "registration/create_profile_page.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class = EditProfilePageForm
    template_name = "registration/edit_profile_page.html"
    success_url = reverse_lazy('home')

class ShowProfilePage(DetailView):
    model = Profile
    template_name = "registration/user_profile.html"

    def get_context_data(self, *args, **kwargs):
        user = Profile.objects.all()
        context = super(ShowProfilePage, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context
        
        


class PasswordsChangeViews(PasswordChangeView):
    # form_class = PasswordChangeForm
    form_class = PasswordChangeForm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html', {})


class RegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

