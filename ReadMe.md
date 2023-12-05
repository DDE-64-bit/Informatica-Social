
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
  python -m django startproject informatica
```

## Open je website

Blijf nog even in de terminal, type dan het volgende commando in.

```bash
  python manage.py startapp mijnProjectNaam
```

Vervang "mijnProjectNaam" voor de naam van jouw website.

Nu maak je van alle losse vooraf gegenereerde python bestanden één geheel.

Voer dan dit commando uit, om je website te laten zien op localhost (dan staat de website alleen voor jouw online).

```bash
  python manage.py runserver 4000
```

Nu kan je naar [localhost](https://127.0.0.1:4000). Dit is jouw eigen site!

Om de server uit te zetten druk de toetsen ctrl + c in.


## Bewerk jouw website

Nu ga jij de website personaliseren. Eerst moet je naar windows verkenner en dan naar de folder met jouw project erin.

Als het goed is zie je dan 2 folders, 1 python bestand en een database bestand. 

Open de map met "mijnProjectNaam". Dan heb je 1 folder en 6 python bestanden.

Open het bestand "views.py" met thonny.

In het bestand staat dit.

```bash
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

Ga naar de folder met jouw project erin. Open de folder genaamd informatica.

Open dan het bestand genaamd "urls.py", haal het commetaar weg.

Voeg dan deze code toe.

```python
  from . import views # Voeg het bestand views toe aan dit python bestand
```

In de list "urlpatterns" verwijder deze regel code.

```python
  path('admin/', admin.site.urls),
```

Voeg daar deze regel code aan toe.

```python
  path("", views.index, name="index"), # Van het bestand views voeg de functie index toe aan de webpagina
```