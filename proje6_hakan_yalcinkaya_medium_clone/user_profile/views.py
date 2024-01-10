from django.contrib import messages
from django.contrib.auth import authenticate, login
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
        print(username, password)
        # bu bilgileri dogru aldik mi?
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # login oldugunu kullaniciya belli edelim!
            messages.success(request, f"{request.user.username} Login oldun")
            # login oldugunu kullaniciya belli edelim!
            return redirect("home_view")

    return render(request, "user_profile/login.html", context)
