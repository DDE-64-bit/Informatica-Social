from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import redirect
from django.contrib .auth.models import User, auth
from django.contrib import messages
from .models import Profile

def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def aanmelden(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Gegevens zijn verkeerd')
                return redirect('aanmelden')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Gegevens zijn verkeerd')
                return redirect('login')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #log user in and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('login')
        else:
            messages.info(request, 'Wachtwoorden verschillen')
            return redirect('aanmelden')
        
    else:
        return render(request, 'aanmelden.html')