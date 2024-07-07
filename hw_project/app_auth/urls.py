from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm

app_name = "app_auth"

# urlpatterns = [
#     path('signup/', views.RegisterView.as_view(), name='signup'),
#     path('login/',
#          LoginView.as_view(template_name='app_auth/login.html', form_class=LoginForm, redirect_authenticated_user=True),
#          name='login'),
#     path('logout/', LogoutView.as_view(template_name='app_auth/logout.html'), name='logout')
# ]


urlpatterns = [
    path('signup/', views.RegisterView.as_view(), name='signup'),
    path('signin/',
         LoginView.as_view(template_name='app_auth/login.html', form_class=LoginForm, redirect_authenticated_user=True),
         name='signin'),
    # path('signin/', LoginView.as_view(template_name='app_auth/login.html', form_class=LoginForm), name='signin'),
    path("logout/", LogoutView.as_view(template_name='app_auth/logout.html'), name="logout")
]

# urlpatterns = [
#     path("register/", views.RegisterView.as_view(), name="register"),
#     path("login/", LoginView.as_view(redirect_authenticated_user=True, template_name='app_auth/login.html',
#                                      authentication_form=LoginForm), name="login"),
#     path("logout/", LogoutView.as_view(template_name='app_auth/logout.html'), name="logout")
# ]