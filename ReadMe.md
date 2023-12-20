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