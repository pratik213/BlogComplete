from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from . forms import SignUpForm,EditProfileForm,PasswordChangingForm,ProfilePageForm
from  myblog.models import Profile


class CreateProfilePageView(generic.CreateView):
    model=Profile
    form_class=ProfilePageForm
    template_name="registration/create_profile_page.html"

    # fields='__all__'

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)



class EditProfilePageView(generic.UpdateView):
    model=Profile
    template_name="registration/edit_profile_page.html"
    fields=['profile_pic','bio','website_url','fb_url','insta_url','linkedin_url']
    success_url=reverse_lazy('home')
    
class ShowProfilePageView(generic.DetailView):
    model=Profile
    template_name="registration/profile.html"

    def get_context_data(self,*args ,**kwargs):
        # users=Profile.objects.all()
        context=super(ShowProfilePageView,self).get_context_data(*args ,**kwargs)
        page_user=get_object_or_404(Profile,id=self.kwargs['pk'])
        context["page_user"]=page_user
        return context

class UserRegisterView(generic.CreateView):
    form_class=SignUpForm
    template_name="registration/register.html"
    success_url=reverse_lazy('home')

class UserEditView(generic.UpdateView):
    form_class=EditProfileForm
    template_name="registration/edit_profile.html"
    success_url=reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class=PasswordChangingForm
    success_url=reverse_lazy('password_sucess')

def password_sucess(request):
    return render(request,"registration/password_sucess.html",{})