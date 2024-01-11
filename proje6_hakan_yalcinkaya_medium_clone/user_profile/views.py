from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def login_view(request):
    # login olan kullanici direkt olarak ana sayfaya gitsin.
    if request.user.is_authenticated:
        # zaten loginsin!!!
        messages.info(request, f"{request.user.username} Daha Önce Login Olmuşsun")
        # zaten loginsin!!!
        return redirect("home_view")
    # login olan kullanici direkt olarak ana sayfaya gitsin.

    context = dict()
    if request.method == "POST":
        # print(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        # bu bilgileri dogru aldik mi?
        messages.success(
            request, f"Kullanıcı adı ve şifre  6 karakterden küçük olamaz!"
        )
        # bu bilgileri dogru aldik mi?
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # login oldugunu kullaniciya belli edelim!
            if len(username) < 6 or len(password) < 6:
                messages.success(request, f"{request.user.username} Login oldun")
                return redirect("user_profile:login_view")
            # login oldugunu kullaniciya belli edelim!
            return redirect("home_view")

    return render(request, "user_profile/login.html", context)


def logout_view(request):
    messages.info(request, f"{request.user.username} Oturumun kapatıldı.")
    logout(request)
    return redirect("home_view")


def register_view(request):
    context = dict()
    if request.method == "POST":
        print(request.POST)
    return render(request, "user_profile/register.html", context)
