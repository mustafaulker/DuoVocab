from django.contrib import admin
from django.urls import path

import DuoVocabFE.views as views

app_name = "DuoVocabFE"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.homepage, name="homepage"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("known_words/", views.known_words, name="known_words"),
]
