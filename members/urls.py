
from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.UserRegisterView.as_view(),name="register"),
    path('edit_profile/',views.UserEditView.as_view(),name="edit_profile"),
    path('password/',views.PasswordsChangeView.as_view(template_name="registration/change-password.html")),
    path('password-sucess',views.password_sucess,name="password_sucess"),
    path('<int:pk>/profile',views.ShowProfilePageView.as_view(),name="show_profile_page"),
    path('<int:pk>/edit_profile_page/',views.EditProfilePageView.as_view(),name="edit_profile_page"),
    path('create_profile_page/',views.CreateProfilePageView.as_view(),name="create_profile_page"),
    # path('password/',auth_views.PasswordChangeView.as_view(template_name="registration/change-password.html"))
]
