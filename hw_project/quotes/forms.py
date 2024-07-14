from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django import forms
from django.contrib.auth.models import User
from django.db import models
from .models import Author, Quote, Tag


class YourRegisterForm(UserCreationForm):
    # Добавьте любые дополнительные поля или настройки, если необходимо
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        # Ваша логика проверки электронной почты здесь
        pass


def register(request):
    if request.method == "POST":
        form = YourRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("your-redirect-url")
    else:
        form = YourRegisterForm()
    return render(request, "registration/register.html", {"form": form})


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["fullname", "born_date", "born_location", "description"]


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']
        widgets = {
            'tag': forms.CheckboxSelectMultiple()
        }