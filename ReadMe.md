
# Django

Voor informatica ga jij met python een website maken. Daarvoor ga jij Django gebruiken, hieronder kun je zien hoe je kan beginnen. 

## Instaleer Django

Nu ga jij Django instaleren. Dat doe je door in de windows zoekbalk "cmd" te typen en op enter te drukken. Dan zie jij als het goed is een zwart scherm. type daar het onderstaande commando in.

```bash
  pip install Django
```

Als je dat hebt gedaan dan ga jij naar het bureaublad (Desktop). Druk dan met je rechtermuisknop op het bureaublad, dan krijg je een lijstje met opties. Druk dan op "Openen met Terminal". 

Dan krijg je ook een zwart scherm.


## Maak je project

Nu je in dat terminal zit, type je dit commando.

```bash
  python -m django startproject mijnSite
```

## Open je website

Blijf nog even in de terminal, type dan het volgende commando in.

```bash
  ren mijnSite django
  cd django
  python manage.py startapp mijnProject
```

Nu maak je van alle losse vooraf gegenereerde python bestanden één geheel.

Voer dan dit commando uit, om je website te laten zien op localhost (dan staat de website alleen voor jouw online).

```bash
  python manage.py runserver 4000
```

Nu kan je naar [localhost](https://127.0.0.1:4000). Dit is jouw eigen site!

Om de server uit te zetten druk de toetsen ctrl + c in.


## Bewerk jouw website

Nu ga jij de website aanpassen. Open de folder django.

Als het goed is zie je dan 2 folders, 1 python bestand en een database bestand. 

Open de folder die mijnProject heet. Dan heb je 1 folder en 6 python bestanden.

Open het bestand "views.py" met thonny.

In het bestand staat dit.

```python
  from django.shortcuts import render

  # Create your views here.
```

Haal het commetaar weg.

Type vervolgens deze code (het commetaar is niet nodig, het kan wel handig zijn.)

```python
  from django.http import HttpResponse
  # Je voegt hier van Django "hyper text transfer protocol" toe

  def index(request): # Maak de functie index met als invoer een "request"
    return HttpResponse("Welkom bij deze enquête") # Stuur een http reactie terug
```

Ga terug naar de folder die mijnProject heet.

Maak daar een nieuw bestand aan met de naam "urls.py".

Open dat bestand in thonny en voeg deze code toe.

```python
  from django.urls import path
  from . import views # Voeg "views.py" toe aan dit programma

  urlpatterns = [
    path("", views.index, name="index"), # Voeg de pagina 
  ]
```

Nu ga je zorgen dat hij automatisch de functie index laad als je de site opent.

Ga naar de folder "django"

Open dan de folder die "mijnSite" heet, daarin staat ook een  bestand genaamd "url.py". 

Open dat bestand in thonny.

Type deze code in

```python
from django.contrib import admin
from django.urls import include, path # Voeg de url van

urlpatterns = [
    path('', include('mijnProject.urls')),  # Dit zorgt ervoor dat het script urls word geimporteerd
    path('admin/', admin.site.urls),
]
```



python --version
pip --version
python -m install django
//create django thing

python -m django startproject social

social
    manage.py
    social/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py

python manage.py runserver 4000

py manage.py startapp members

socail
    manage.py
    social/
    members/
        migrations/
            __init__.py
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py

/members/views.py:
  vervang alles met dit:
```python
from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")
```

def members heet members omdat het over de app members gaat.


als je app of view aanmaakt dan heb je ook een bijbehorende url nodig


maak een bestand genaamt urls.py in de folder members. typ daar deze code
/members/urls.py:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
]
```

dit zorgt ervoor dat er een path is genaamd localhost:4000/members. en dat die een view met de naam members laat zien

ga dan naar je hooft map waar manage.py in staat. ga dan naar de folder die social heet.

zorg dat dit element word geimporteerd:"from django.urls import include, path"

voeg aan urlpatterns dit toe: "path('', include('members.urls')),"  

als je nu de command python manage.py runserver 4000 uitvoert en dan 

localhost:4000/members opzoekt krijg je hello world te zien

maak een template folder in de members folder.
maak daar een bestand genaamd index.html

index is de standaart naam voor een html pagina.

voeg daar deze standaard html code in:


// eigen notitie voeg comments toe
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Hello world</h1>
    <p>Welkom op mijn members pagina</p>
</body>
</html>
```

ga dan naar views.py en voeg deze code toe om de index.html pagina te laden wanneer de view members word gebruikt.

import dit"from django.template import loader"

en voeg deze regel toe aan def member():
```python
template = loader.get_template('index.html')
```

wat dit doet is het maakt een variable voor de template. en gebruikt de libery loader om index.html te laden.

open social/settings.py. dit is een vol bestand schrik niet zoek de list genaamd INSTALD_APPS.

voeg daar 'members' aan toe


Dan moet je de juiste liberys download/update. dat doe je zo:

```bash
py manage.py migrate
```

vervang de members view door:

```python
def members(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
```

Start dan de je project met dit comman:
```bash
py manage.py runserver
```

Nu hebben wij alleen maar vaste html code laten zien, in django kan je ook data uit een database weergeven, die data heet in django models.


ga open het bestand models.py. Maak daar een class aan met de naam "Member" geef als waarde models.Model mee.

Voeg daar op deze manier een model toe:

```python
voorNaam = models.CharField(max_length=255)
```

Doe dit op dezelfde manier voor achterNaam.


Run dit command om de database aan te passen
```bash
py manage.py makemigrations members
```

Nu is er een migrations folder in de map van models.py

Open het bestand dat "0001_initial.py" heet.

Daar zie je dat django automatisch een colorm id heeft aangemaakt.

run dit command om de database te updaten
```bash
py manage.py migrate
```

