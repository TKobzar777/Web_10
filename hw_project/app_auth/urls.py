from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomPasswordResetForm
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name = 'app_auth'

urlpatterns = [
    path('signup/', views.RegisterView.as_view(), name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='app_auth/login.html'), name='signin'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app_auth/logout.html'), name='logout'),

    path('reset-password/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('reset-password/done/', PasswordResetDoneView.as_view(template_name='app_auth/password_reset_done.html'),
         name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='app_auth/password_reset_confirm.html',
                                          success_url='/auth/reset-password/complete/'),
         name='password_reset_confirm'),
    path('reset-password/complete/',
         PasswordResetCompleteView.as_view(template_name='app_auth/password_reset_complete.html'),
         name='password_reset_complete'),
]
#     # Password reset URLs
#     path('password_reset/', auth_views.PasswordResetView.as_view(
#         template_name='app_auth/password_reset.html',
#         email_template_name='app_auth/password_reset_email.html',
#         subject_template_name='app_auth/password_reset_subject.txt',
#         form_class=CustomPasswordResetForm,
#         success_url=reverse_lazy('app_auth:password_reset_done')
#     ), name='password_reset'),
#     path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
#         template_name='app_auth/password_reset_done.html'
#     ), name='password_reset_done'),
#     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
#         template_name='app_auth/password_reset_confirm.html',
#         success_url=reverse_lazy('app_auth:password_reset_complete')
#     ), name='password_reset_confirm'),
#     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
#         template_name='app_auth/password_reset_complete.html'
#     ), name='password_reset_complete'),
# ]