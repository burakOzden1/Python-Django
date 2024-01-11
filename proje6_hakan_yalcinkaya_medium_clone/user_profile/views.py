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
        post_info = request.POST
        email = post_info.get("email")
        email_confirm = post_info.get("email_confirm")
        first_name = post_info.get("first_name")
        last_name = post_info.get("last_name")
        password = post_info.get("password")
        password_confirm = post_info.get("password_confirm")
        instagram = post_info.get("instagram")
        print("*" * 30)
        print(
            email,
            email_confirm,
            password,
            password_confirm,
            first_name,
            last_name,
            instagram,
        )

        if len(first_name) < 3 or len(last_name) < 3 or len(email) < 3 or len(password):
            messages.warning(
                request, "İsim ve Soyisim bilgileri en az 3 karakterden oluşmalıdır!"
            )
            return redirect("user_profile:register_view")

        if email != email_confirm:
            messages.warning(
                request, "Lütfen Eposta bilgisini doğru girdiğinizden emin olunuz."
            )
            return redirect("user_profile:register_view")

        elif password != password_confirm:
            messages.warning(
                request, "Lütfen şifrenizi doğru girdiğinizden emin olunuz."
            )
            return redirect("user_profile:register_view")

        print("*" * 30)
        # print(request.POST)  # kullanicinin bilgilerini konsolda gostedik.
    return render(request, "user_profile/register.html", context)
