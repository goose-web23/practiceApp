from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render


def login_view(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect("dashboard_home")
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:
            login(request, user)

            if user.is_staff:
                return redirect("dashboard_home")

            return redirect("home")

        return render(
            request,
            "accounts/login.html",
            {"error": "Неверный логин или пароль."},
        )

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("home")