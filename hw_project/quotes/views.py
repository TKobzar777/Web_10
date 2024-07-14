from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View, generic
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from django.core.paginator import Paginator
from .forms import TagForm, AuthorForm, QuoteForm
from .models import Quote, Author, Tag

from .utils import get_mongodb


class AuthDetailView(generic.DetailView):
    model = Author

"""Функция main использовалась для загрузки основной страницы из MongoDB"""
def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})
    # return render(request, 'quotes/index.html, context={}')


class HomeView(ListView):
    model = Quote
    template_name = 'home.html'
    context_object_name = 'quotes'
    paginate_by = 7

class QuotesToTag(ListView):
    model = Quote
    template_name = 'home.html'
    context_object_name = 'quotes'
    paginate_by = 7

    def get_queryset(self):
        return Quote.objects.filter(tags__slug=self.kwargs['tags__slug'])

class AddTagView(LoginRequiredMixin, CreateView):
    login_url = "/users/login/"
    model = Tag
    template_name = "quotes/add_tag.html"
    success_url = reverse_lazy('home')
    form_class = TagForm


class AddAuthorView(LoginRequiredMixin, CreateView):
    login_url = "/users/login/"
    model = Author
    template_name = "quotes/add_author.html"
    success_url = reverse_lazy('home')
    form_class = AuthorForm


class AddQuoteView(LoginRequiredMixin, CreateView):
    login_url = "/users/login/"
    model = Author
    template_name = "quotes/add_quote.html"
    success_url = reverse_lazy('home')
    form_class = QuoteForm

