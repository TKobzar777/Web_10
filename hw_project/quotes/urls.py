from django.urls import path
from .views import AddTagView, AddAuthorView, AddQuoteView, AuthDetailView

app_name = "quotes"

urlpatterns = [
    path("add_tag/", AddTagView.as_view(), name='add_tag'),
    path('add_author/', AddAuthorView.as_view(), name='add_author'),
    path('add_quote/', AddQuoteView.as_view(), name='add_quote'),
    path("author/<pk>/", AuthDetailView.as_view(), name="author_detail"),

]
