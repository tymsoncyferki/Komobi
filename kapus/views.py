from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from kapus.models import *
from datetime import datetime


def index(request):
    return render(request, 'kapus/index.html')


def map(request):
    if not request.user.is_authenticated:
        return redirect('kapus:login')
    issues = Issue.objects.all()

    return render(request, 'kapus/map.html', {"issues": issues})


def issue(request, issue_id):
    i = get_object_or_404(Issue, id=issue_id)
    return render(request, 'kapus/issue.html', {"issue": i})


def history(request):
    issues = Issue.objects.all().order_by('time')

    return render(request, 'kapus/history.html', {"issues": issues})


def issue_form(request):
    if request.method == "POST":
        title = request.POST['title']
        category = request.POST['category']
        description = request.POST['description']
        lat = request.POST['lat']
        long = request.POST['long']

        issue = Issue(title=title, category=category, description=description, latitude=lat, longitude=long)
        issue.save()
        photo = request.POST['photo'] + str(issue.id)
        issue.photo = photo
        issue.save()
        return redirect('kapus:issue', issue_id=issue.id)

    lat = request.GET.get('lat')
    long = request.GET.get('long')

    categories = ['Infrastruktura', 'Bezpieczeństwo', 'Komunikacja miejska']

    return render(request, 'kapus/issue_form.html', {'lat': lat, 'long': long, 'categories': categories})


def login_view(request):
    if request.method == 'POST':
        username = request.POST["uname"]
        password = request.POST["psw"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('kapus:account')
        else:
            message = "Wrong username or password"
            return render(request, 'kapus/registration/login.html', {"message": message})
    if request.user.is_authenticated:
        return redirect('kapus:account')
    else:
        return render(request, 'kapus/registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('kapus:login')


def register_view(request):
    if request.method == 'POST':
        email = request.POST["email"]
        username = request.POST["uname"]
        city = request.POST["city"]
        password = request.POST["psw"]
        password2 = request.POST["psw2"]
        try:
            u = User.objects.get(email=email)
            message = "There is already an account associated with this email address"
            return render(request, 'kapus/registration/register.html', {"message": message})
        except ObjectDoesNotExist:
            pass
        try:
            u = User.objects.get(username=username)
            message = "This username is already taken"
            return render(request, 'kapus/registration/register.html', {"message": message})
        except ObjectDoesNotExist:
            pass
        try:
            assert password == password2
        except AssertionError:
            message = "Passwords do not match"
            return render(request, 'kapus/registration/register.html', {"message": message})

        user = User(email=email, username=username, first_name=city)
        user.set_password(password)
        user.save()
        login(request, user)

    if request.user.is_authenticated:
        return redirect('kapus:account')
    else:
        cities = ['Katowice', 'Warszawa', 'Poznan', 'Krakow', 'Gdansk', 'Szczecin', 'Jazgarzewszczyzna']
        return render(request, 'kapus/registration/register.html', {'cities': cities})


def account(request):
    if request.user.is_authenticated:
        return render(request, 'kapus/registration/account.html', {"user": request.user})
    else:
        return redirect('kapus:login')
