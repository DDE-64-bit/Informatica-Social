<h1>Project opzetten</h1>


django-admin startproject "projectname"

django-admin startapp core

ga naar /core en maak het bestand urls.py

voeg deze code toe aan het bestand /core/urls.py
``` python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

nu heb je een url aangemaakt voor de hoofd pagina van jouw site. 

ga  nu naar /core/views.py.


importeer deze libery's.

```python
from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import redirect
from django.contrib .auth.models import User, auth
from django.contrib import messages
```


Voeg dan deze code toe om een view te maken.

```python
def index(request):
    return render(request, "index.html")
```

Nu heb je door middel van een functie een 'view' aangemaakt, dat is een webpagina. We komen later nog terug op wat al die request en renders doen.

Probeer nu eens naar jouw website te gaan, dat doe je door deze onderstaande commando's in je terminal te typen.

```bash
cd {projectnaam}
```
Nu gebruik je het cd commando, dat staat voor change directory. Je gaat dus naar een andere folder via de commandline. 

Nu heb je een stap die je niet vaak hoeft te doen, dat is je database migreren. Dat doe je door dit commando in te vullen.

```bach
python manage.py migrate
```

Voer nu het laatste commando uit om de server te starten.

```bash
python manage.py runserver 4000
```
Nu gebruik je python om het bestand ./manage.py te openen. Runserver betekend dat je de website opstart. de 4000 staat voor de poort die je gebruikt om naar de site te gaan. 

4000 is de debug poort, voor http gebruik je 8080 en voor https gebruik je 443. We komen daar later ook nog op terug, dus gebruik 4000.

Dan zie je in de terminal iets zien zoals dit.
```bash
Django version 5.0.1, using settings '{projectnaam}.settings'
Starting development server at http://127.0.0.1:4000/
Quit the server with CONTROL-C.
```

Druk dan de control key in en druk op "https://127.0.0.1:4000/".

Dit brent je naar jouw website. Dan zie je een standaard pagina.

Ga terug naar jouw terminal en druk op control + c om je server af te sluiten.

Type dan de volgende commando's in.

``` bash
cd ..
```
Weer change directory, maar dit keer met 2 punten, dat betekend dat je weer terug gaat naar de map die boven je huidige map ligt.

```bash
mkdir templates
```

Nu gebruik je het mkdir commando om een map aan te maken met de naam templates.

**LET OP: Dat de map echt templates heet ander krijg je later problemen.**

Open dan /{projectnaam}/settings.py, zoek dan naar het onderstaande stukje code.

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

Vervang dan de regel:
```python
"DIRS": [],
```

Voor:

```python
"DIRS": [os.path.join(BASE_DIR, "templates")],
```

Ga dan naar de bovenkant van het script, importeer daar deze libery.

```python
import os
```

Zoek de list "INSTALLED_APPS" op voeg onderaan deze list dit toe.

``` python
"core",
```


Ga terug naar jouw terminal, probeer nu eens zelf in de folder templates te komen.

Als dat is gelukt dan ga je een bestand aanmaken via de cli (terminal), dat doe je zo.

``` bash
touch index.html
```

Daarna ga je het bestand openen, dat kan ook via de cli.

``` bash
code index.html
```

Als het geopend is, druk dan op ! en daarna meteen tab of enter. Dan verschijnd er een stuk code, dit is html.


Open nu het bestand /{projectnaam}/urls.py.

Importeer deze libery's.

```python
from django.conf import settings
from django.conf.urls.static import static
```

En verander deze regel.

```python
from django.urls import path
```

Naar dit

```python
from django.urls import path, include
```

Voeg aan urlpatterns dit path toe.

```python
path('', include('core.urls'))
```

Start nu je site op, als alles goed is gegaan zie je nu een lege pagina.

<br><br>

<h1>HTML/CSS</h1>
Nu kan je naar w3schools gaan en zelf oefenen met html en css. Je hoeft niet alles te weten hieronder heb je links naar alle belangerijke onderwerpen.

<br>

<h3>Deze zijn nodig om te weten:</h3>

* [Koptitels](https://www.w3schools.com/html/html_headings.asp)
* [Paragrafen](https://www.w3schools.com/html/html_paragraphs.asp)
* [Stijlen](https://www.w3schools.com/html/html_formatting.asp)
* [Afbeeldingen](https://www.w3schools.com/html/html_images.asp)
* [Titel](https://www.w3schools.com/html/html_page_title.asp)
* [Div](https://www.w3schools.com/html/html_div.asp)
* [Formulieren](https://www.w3schools.com/html/html_forms.asp)
* [Syntax (css)](https://www.w3schools.com/css/css_syntax.asp)
* [Kleuren (css)](https://www.w3schools.com/css/css_colors.asp)
* [Achtergrond (css)](https://www.w3schools.com/css/css_background.asp)
* [Hoogte/Breedte (css)](https://www.w3schools.com/css/css_dimension.asp)
* [Formulieren (css)](https://www.w3schools.com/css/css_form.asp)



<h3>Voor extra verdieping</h3>

* [Commentaar](https://www.w3schools.com/html/html_comments.asp)
* [Favicon](https://www.w3schools.com/html/html_favicon.asp)
* [Lay-out](https://www.w3schools.com/html/html_layout.asp)
* [Bestanden Locatie](https://www.w3schools.com/html/html_filepaths.asp)
* [Externe css (css)](https://www.w3schools.com/css/css_howto.asp)
* [Marge (css)](https://www.w3schools.com/css/css_margin.asp)
* [Tekst (css)](https://www.w3schools.com/css/css_text.asp)

<br>

**Tip: Er staat bij w3schools vaak een "Try it Yourself" knop, daar kan makkelijk oefenen met html en css.**


!!! overleg dit eerst met docent !!!

Als je html en css door denkt te hebben, probeer dan een mooie thuispagina te maken voor jouw site. Kies een leuk thema uit voor jouw site (probeer creatief te zijn).


<br><br>

<h1>Databases</h1>

<h3>Inloggen en registreren</h3>

Maak eerst een html pagina met een formulier met de velden username en password, zorg dat er ook een submit knop is.

Als je die in jouw template map hebt staan met de naam login.html.

Zorg dat bij de tag form het atribuut action leeg is en dat je het atribuut method="post" toegevoegd is.

Dan zou het er ongeveer zo uitziet (wel opgemaakt met css).

```html
<form action="" method="POST">
    <input type="text" name="username" placeholder="Gebruikersnaam">
    <input type="password" name="password" placeholder="Wachtwoord">

    <button type="submit">Login</button>
    <div>
        <p> Niet geregistreerd? <a href="/aanmelden"> Create a account </a></p>
    </div>
</form>
```

**LET OP: Zorg dat de name="" gelijk is met de bovenstaande stukje code, ander krijg je daar problemen mee.**

Voeg daarna onder de tag form deze regel toe, dit is van groot belang omdat dit voorkomt dat jouw website kwetsbaar is voor [Cross-Site Request Forgery](https://owasp.org/www-community/attacks/csrf).


```html
{% csrf_token %}
```

Oke nu gaan we terug naar /core/urls.py, voeg deze regel toe aan urlpatterns.

```pyhton
path('login', views.login, name='login'),
```

Ga dan naar /core/views.py. Maak daar een nieuwe functie aan met de naam login, die als parameter request heeft.

Return dan de webpagina met de functie render, net zoals bij def index().

Als je dat hebt gedaan kan je nu jouw website opstarten. Wanneer de website is opgestart ga dan naar jouw site, vul dan in de url bar achter het adres van jouw site /login in en druk op enter. 

Dan zie je de login pagina.

Als je op de submit knop drukt zie als het goed is in jouw terminal iets zoals dit staan.

```bash
[**/***/**** **:**:**] "POST /login HTTP/1.1" 200 699
```

Op de sterretjes staat de datum en tijd.

Als jouw formulier geen POST maar een GET geeft, dan ben je vergeten om je method naar POST te veranderen (kijk dan terug hoe je dat moet doen).


Maak nu een html bestand voor het aanmeleden, zorg dat je de velden username, mail, password en repeat password hebt. 

Als je dat hebt ziet je code er ongeveer zo uit (wel met css).

```html
<form action="" method="POST">
    {% csrf_token %}
    <input type="text" name="username" placeholder="Gebruikersnaam">
    <input type="email" name="email" placeholder="Mail">
    <input type="password" name="password" placeholder="Wachtwoord"">
    <input type="password" name="password2" placeholder="Herhaal wachtwoord">

    <button type="submit">Sign Up</button>
    <div>
        <p> Heb je al een account? <a href="/login"> Login </a></p>
    </div>
</form>
```

**LET OP: Zorg dat de name="" gelijk is met de bovenstaande stukje code, ander krijg je daar problemen mee.**


Nu gaan je weer naar /core/urls.py, voeg daar een path toe voor aanmelden.

Ga dan naar /core/models.py, importeer daar deze libery.

```python
from django.contrib.auth import get_user_model
```

Voeg daarna deze code toe.

```python
user = get_user_model()
```

Dit maakt een variable aan die user heet en die is gelijk aan de return van get_user_model(), dat is de standaart inlog functie van django. Maak daaronder een class aan die er zo uitziet.

```python
class Profile(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    
    def __str__(self):
        return self.user.username
```

Ga daarna naar views.py, voeg daar deze code toe.

```python

```