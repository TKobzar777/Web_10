from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from quotes.views import HomeView




# urlpatterns = ([
#     # path("admin/", admin.site.urls),
#     # path("", include("quotes.urls")),
#     # path("auth/", include('app_auth.urls')),
#     # path("admin/", admin.site.urls),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include('app_auth.urls')),
    path("quotes/", include('quotes.urls')),
    path('', HomeView.as_view(), name='home')
    # path("", include('quotes.urls')),
    # path("", HomeView.as_view(), name='home')
]
# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("", include("quotes.urls")),
#     # path("users/", include("users.urls"))
# ]
