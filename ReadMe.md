create project, stappen staan hierboven social1

create app core
run project

URL ROUTING

in /core maak een bestand genaamt urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
```

open views.py

voeg dit toe
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welkom op Het Streek sociaal</h1>")
```

ga naar /social1/urls.pys

zorg dat dit er staat:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'))
]
```

test of het werkt.

open social1/settings.py

import os
voeg aan installed apps de app 'core' toe

zoek templates

maak dan een folder genaamt templates toe aan de map waar ook manage.py in staat.

vul bij dit: 'DIRS': [],

dit in: 'DIRS': [os.path.join(BASE_DIR, 'templates')],  

stop dan alle gedownloade html bestaden in de map templates.

- index
- profile
- settings
- signin
- signup

ga terug naar /core/views.py

vervang dit: return HttpResponse("<h1>Welkom op Het Streek sociaal</h1>")

voor dit: return render(request, "index.html")


kijk op de website. als het goed is zie je nu iets anders, maar het ziet er niet goed uit.



naast de folder templates maken wij nu ook een folder genaamt static aan.

ga terug naar /social1/setting.py

onder: STATIC_URL = 'static/' 

voeg dit toe: 

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

voeg de andere gedownloade bestanden toe.
- assets
- css
- fonts
- images
- js
- settings
- video

!! 32.39

open index.html

open /core/models.py

ga naar de hoofd map en maak daar een folder aan genaamd: media

open settings.py

voeg onderaan dit bestand deze code toe: 

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

open nu het bestand /social1/urls.py

import deze liberys: 
from django.conf import settings
from django.conf.urls.static import static


voeg ook deze regel in: urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

verplaats: blank-profile-picture.png naar de /media folder


ga terug naar models.py

voeg deze code in:

from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to="profile_images", default="blank-profile-picture.png")
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


nu gaan we de database migreren.

run dan nu de commando: python manage.py makemigrations
python manage.py migrate

open /core/admin.py

voeg deze code toe:
from .models import Profile

admin.site.register(Profile)




admin account maken.

python manage.py createsuperuser

zet de server nu aan

kijk op jouw site op de url localhost:4000/admin

log in met jouw zojuist aangemaakte gegevens

druk dan op profiles. als het goed is zie je nog geen profielen


aanmelden


!! 10055

open /core/urls.py

voeg daar deze regel aan toe in urlpatterns.
path('signup', views.signup, name='signup'),

open /core/views.py

voeg deze functie toe: 

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #log user in and redirect to settings page
                # komt later

                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('signup')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
        
    else:
        return render(request, 'signup.html')



en importeer deze libery's

from django.shortcuts import redirect
from django.contrib .auth.models import User, auth
from django.contrib import messages
from .models import Profile


start nu je server en ga naar 127.0.0.1:4000/signup zie je iets?
probeer eens een account aan te maken. ga dan naar 127.0.0.1:4000/admin en log in met je superuser
druk dan op profiles. zie jij jouw account staan?

ga naar core/views.py



signin and login

ga naar core/urls.py

voeg deze url toe aan de urlpatterns:
path("signin", views.signin, name="signin"),

ga naar /core/views.py

en voeg deze view toe:

def signin(request):
    return render(request, "signin.thml")

ga nu eens naar de pagina die je zojuist hebt aangemaakt.

oke, ga nu weer terug naar je views.py

        maak dan een if else functie die kijkt of de request method gelijk is aan POST (kijk terug bij de signup view als jee het niet meer weet)
"vraag docent of bovenstaande goed is"
zo niet dan dit


voeg deze view toe aan /core/views.py

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None: # kijkt of de user bestaat
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Credentials Invalid")
            return redirect("signin")
        
    else:
        return render(request, "signin.html")




maak een nieuw url aan voor logout
doe dat zo: 

path("logout", views.logout, name="logout"),

ga naar core/views.py

voeg daar deze simpele functie aan toe:
def logout(request):
    auth.logout(request)
    return redirect("signin")

sla op en ga naar jouw webpagina, druk op jouw profiel foto (rechts boven) en dan logout

maar nu kan je nog steeds op de hoofdsite als je bent uitgelogd, dat gaan wij veranderen.

importeer deze libery:
from django.contrib.auth.decorators import login_required

in /core/views.py

voeg dan deze code toe aan de regel direct boven def index() en boven def logout():
@login_required(login_url="signin")


probeer nu eens naar de main page te gaan. als dat lukt druk dan op logout, als het goed is word je gevraagt om in te loggen.



    	
Account settings:

ga naar /core/urls.py

maak daar een url aan met de naam settings

ga dan naar views.py en maak daar een settings view:

@login_required
def settings(request):
    return render(request, "settings.html")


ga nu naar de functie van de view signup. voeg waar je eerst # komt later had ingevult dit toe: 
    user_login = auth.authenticate(username=username, password=password)
    auth.login(request, user_login)

en verander nog steeds in hetzelfde deel van de if-else functie de 

return redirect('signup')

naar:
return redirect('settings')
