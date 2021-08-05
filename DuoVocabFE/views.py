import duolingo
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import NewUserForm
from .models import DuoData, LangAbrv


def homepage(request):
    return render(request, "home.html", {})


@login_required
def profile(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if not DuoData.objects.filter(user_id=request.user.id).exists():
            duo_user = duolingo.Duolingo(username, password)
            words_by_language, translations = {}, {}
            for lang_abrv in duo_user.get_languages(abbreviations=True):
                words_by_language[lang_abrv] = duo_user.get_known_words(lang_abrv)
            for source in words_by_language:
                translations[source] = duo_user.get_translations(target='en', source=source,
                                                                 words=words_by_language[source])
            user_info = duo_user.get_user_info()
            DuoData.objects.get_or_create(user_id=request.user.id,
                                          username=username,
                                          password=password,
                                          duo_id=user_info['id'],
                                          fullname=user_info['fullname'],
                                          bio=user_info['bio'],
                                          location=user_info['location'],
                                          account_created=user_info['created'].strip('\n'),
                                          avatar=str(user_info['avatar']) + '/xxlarge',
                                          known_words=words_by_language,
                                          translations=translations,
                                          languages=duo_user.get_languages(),
                                          lang_abrv=duo_user.get_languages(abbreviations=True))

    return render(request, "profile.html", {'duo_user': DuoData.objects.filter(user_id=request.user.id).first()})


@login_required
def known_words(request):
    lang_selection = None
    if 'lang_selection_btn' in request.POST:
        lang_selection = LangAbrv.objects.get(name=request.POST['lang_selection_btn']).abrv
        request.session['lang_selection'] = lang_selection
    elif 'random_study_btn' in request.POST:
        return redirect('flashcard')
    return render(request, "known_words.html",
                  {'duo_user': DuoData.objects.filter(user_id=request.user.id).first(),
                   'lang_selection': lang_selection})


@login_required
def flashcard(request):
    card_side = "front"
    word = None
    if 'front' in request.POST:
        card_side = 'back'
        word = request.POST['front']
    elif 'back' in request.POST:
        card_side = 'front'
    return render(request, "flashcard.html",
                  {'duo_user': DuoData.objects.filter(user_id=request.user.id).first(),
                   'card_side': card_side, 'lang_selection': request.session['lang_selection'],
                   'translate_params': [request.session['lang_selection'], word]})


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
