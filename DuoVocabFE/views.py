import duolingo
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import NewUserForm
from .models import DuoData


def homepage(request):
    return render(request, "home.html", {})


def profile(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if not DuoData.objects.filter(user_id=request.user.id).exists():
            duo_user = duolingo.Duolingo(username, password)
            languages = {}
            user_lang = duo_user.get_languages(abbreviations=True)
            for lang in user_lang:
                languages[lang] = duo_user.get_known_words(lang)
            DuoData.objects.get_or_create(user_id=request.user.id,
                                          username=username,
                                          password=password,
                                          known_words=languages,
                                          languages=duo_user.get_languages(abbreviations=True))

    return render(request, "profile.html", {'duo_user': DuoData.objects.filter(user_id=request.user.id).first()})


def known_words(request):
    lang_selection = None
    if request.method == "POST":
        lang_selection = request.POST['button']
    return render(request, "known_words.html",
                  {'duo_user': DuoData.objects.filter(user_id=request.user.id).first(),
                   'lang_selection': lang_selection})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, "auth/register.html", {"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "auth/login.html", {"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("homepage")
