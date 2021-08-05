from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from DuoVocabFE import views

app_name = "DuoVocabFE"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.homepage, name="homepage"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", LogoutView.as_view(), name="'logout"),
    path("profile/", views.profile, name="profile"),
    path("known_words/", views.known_words, name="known_words"),
    path("flashcard/", views.flashcard, name="flashcard"),
]
