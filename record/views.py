from django.shortcuts import render, redirect, reverse, HttpResponse
from user.models import User
from django.contrib.auth.hashers import check_password
from fixed.models import Fixed
from record.models import CurrentRecord


def check_authority(func):
    def wrapper(*args, **kwargs):
        username = args[0].session.get("login_user", "")
        if username != "":
            args[0].session["path"] = args[0].path
            return redirect(reverse("login"))
        return func(*args, **kwargs)
    return wrapper


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
            is_valid = check_password(password, user.password)
        except:
            is_valid = False
        if is_valid:
            request.session["login_user"] = username
            request.session.set_expiry(1209600)
            return redirect(request.session["path"])
        else:
            return HttpResponse("登录失败，请确认用户名和密码是否正确")
    else:
        return render(request, "login.html")
