from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from quotes.views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include('app_auth.urls')),
    path("quotes/", include('quotes.urls')),
    path('', HomeView.as_view(), name='home')

]

