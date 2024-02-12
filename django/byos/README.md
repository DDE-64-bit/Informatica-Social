<h1>Project opzetten</h1>

Om te beginnen met django moet je eerst een project aanmaken. Ga naar de locatie waar het project moet komen. Type dan dit in de terminal.
```bash 
django-admin startproject "projectname"
```

Hiermee maak je een django project aan. 

Nu moet je nog een app hebben in jouw project, dit is de plek waar jij gaat werken. Vul het onderstaande in.
```bash
django-admin startapp core
```

Ga dan naar /core en maak een bestand genaamd urls.py aan.

Voeg deze code toe aan het bestand /core/urls.py.

``` python
from django.urls import path # Om url's te gaan gebruiken
from . import views # Alle views importeren

urlpatterns = [
    path('', views.index, name='index'), # Zorgt dat de hoofd pagina index.html laat zien
]
```

Nu heb je een url aangemaakt voor de hoofd pagina van jouw site. 

Ga dan naar /core/views.py.


Importeer deze libery's.

```python
from django.shortcuts import render # Om html te laden
from django.http import HttpResponse # Om html reacties te krijgen van de gebruiker

from django.shortcuts import redirect # Om door te verwijzen
from django.contrib .auth.models import User, auth # Om in te loggen
from django.contrib import messages # Om vanaf python een bericht in html laten zien
```

Voeg dan deze code toe om een view te maken.

```python
def index(request): # Maak een functie met de naam van de url, geef altijd een request mee (anders werkt het niet)
    return render(request, "index.html") # Wanneer de functie word aangeroepen (de url word geladen) stuur dan de site index.html terug
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
"DIRS": [os.path.join(BASE_DIR, "templates")], # Dit laat jouw site weten waar de html pagina's staan
```

Ga dan naar de bovenkant van het script, importeer daar deze libery.

```python
import os # Om bij je bestanden te kunnen
```

Zoek de list "INSTALLED_APPS" op voeg onderaan deze list dit toe.

``` python
"core", # Om de app core te laden
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
from django.conf import settings # Om de goede instellingen te hebben
from django.conf.urls.static import static # Om eventueel externe scripten te laden
```

En verander deze regel.

```python
from django.urls import path
```

Naar dit

```python
from django.urls import path, include # Om extern url's op te halen
```

Voeg aan urlpatterns dit path toe.

```python
path('', include('core.urls')) # Url's ophalen
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
<form action="" method="POST"> <!--Gebruik POST voor extra veiligheid-->
    <input type="text" name="username" placeholder="Gebruikersnaam"> <!--Gebruikersnaam veld-->
    <input type="password" name="password" placeholder="Wachtwoord"> <!--Wachtwoord veld-->

    <button type="submit">Login</button> <!--Knop om formulier in te sturen-->
    <div>
        <p> Niet geregistreerd? <a href="/aanmelden"> Create a account </a></p> <!--Link naar aanmeldings pagina-->
    </div>
</form>
```

**LET OP: Zorg dat de name="" gelijk is met de bovenstaande stukje code, ander krijg je daar problemen mee.**

Voeg daarna onder de tag form deze regel toe, dit is van groot belang omdat dit voorkomt dat jouw website kwetsbaar is voor [Cross-Site Request Forgery](https://owasp.org/www-community/attacks/csrf).


```html
{% csrf_token %} <!--Om CSRF te voorkomen-->
```

Oke nu gaan we terug naar /core/urls.py, voeg deze regel toe aan urlpatterns.

```python
path('login', views.login, name='login'), # Maak een nieuwe url aan voor jouw site
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
    {% csrf_token %} <!--Tegen CSRF-->
    <input type="text" name="username" placeholder="Gebruikersnaam"> <!--Gebruikersnaam veld-->
    <input type="email" name="email" placeholder="Mail"> <!--Mail veld-->
    <input type="password" name="password" placeholder="Wachtwoord""> <!--Wachtwoord veld-->
    <input type="password" name="password2" placeholder="Herhaal wachtwoord"> <!--Herhaal wachtwoord veld-->

    <button type="submit">Sign Up</button> <!--Inschrijf knop-->
    <div>
        <p> Heb je al een account? <a href="/login"> Login </a></p> <!--Link naar login pagina-->
    </div>
</form>
```

**LET OP: Zorg dat de name="" gelijk is met de bovenstaande stukje code, ander krijg je daar problemen mee.**


Nu gaan je weer naar /core/urls.py, voeg daar een path toe voor aanmelden.

Ga daarna naar views.py, voeg daar deze code toe.

```python
def aanmelden(request): # View voor aanmelden
    if request.method == 'POST': # Gebruik POST voor veiligheid
        username = request.POST['username'] # Link het invoer veld username aan de gebruikersnaam
        email = request.POST['email'] # Link het invoer veld email aan de mail
        password = request.POST['password'] # Link het invoer veld password aan het wachtwoord
        password2 = request.POST['password2']

        if password == password2: # Als de 2 ingevoerde wachtwoorden gelijk zijn dan ...
            if User.objects.filter(email=email).exists(): # Bestaat er al een account met dit mail adres
                messages.info(request, 'Gegevens zijn verkeerd') # Laat in html foutmelding zien
                return redirect('aanmelden') # Reload de site
            elif User.objects.filter(username=username).exists(): # Bestaat deze gebruikersnaam al?
                messages.info(request, 'Gegevens zijn verkeerd') # Laat in html foutmelding zien
                return redirect('login') # Ga naar de login pagina
            else: # Als er een account aangemaakt kan worden
                user = User.objects.create_user(username=username, email=email, password=password) # Maak de gebruiker aan in de database
                user.save() # Sla de gebruiker op

                user_login = auth.authenticate(username=username, password=password) # Sla de gebruiker info op in deze variabele
                auth.login(request, user_login) # Log in

                return redirect('login') # Laad de login pagina
        else:
            messages.info(request, 'Wachtwoorden verschillen') # Laat in html foutmelding zien
            return redirect('aanmelden') # Reload de pagina
        
    else:
        return render(request, 'aanmelden.html') # Als er geen POST is gebruikt, reload de pagina
```

Wat dit doet is het kijkt of er een formulier is ingevuld en als dat is kijk hij naar de gegevens die mee gestuurd worden.

Importeer ook models.py in views.py.

```python
from .models import * # Importeer models
```

Zoals je misschien is opgevallen zie je dat er 3 regels code in staan die met messages.info() werken. Zo kan je een error of een melding aan de user laten zien.

Voeg boven beide formulieren (van aanmelden.html en login.html) dit stukje code toe.

```html
<div>
    <style> /* CSS */
        h5{ /*Deze css is voor alle h5 headers*/
            color: red; /*De kleur van de tekst*/
        }
    </style>
    {% for message in messages %} <!--Deze tekst kan via django aangeroepen worden-->
    <h5>{{message}}</h5> <!--Hier komt het bericht vanuit django-->
    {% endfor %}
</div>
```

Dit zorgd dat je vanuit jouw python code een bericht kan laten zien.

Voordat alle database veranderingen zijn doorgevoerd moeten er nog 2 commando's worden uitgevoerd in de cli.

```bash
python manage.py makemigrations
```

Dit zorgt dat de instellingen worden opgeslagen.

```bash
python manage.py migrate
```

Dit zorgt ervoor dat het word geupdate naar jouw site.

Start nu jouw website ga dan naar /aanmelden. vul dan wat gegevens in. Als de gegevens goed zijn ben je nu op de login pagina, zo niet dan zie je een rood tekstje verschijnen met een fout melding.

Nu moeten wij nog zorgen dat je ook kan inloggen.

Voeg deze code toe aan /core/views.py.

```python
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None: # kijkt of de user bestaat
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Gegevens Ongeldig")
            return redirect("/login")
        
    else:
        return render(request, "login.html")
```


Test nu of je een account kan maken en kan inloggen. Als je bent ingelogd  zie je de index.html site.

Ga terug naar de terminal vul dit in.

```bash
python manage.py createsuperuser
```

Als je dit invuld moet je nog wat andere gegevens invullen (Vul bij wachtwoord niet een veel gebruikt wachtwoord in). Als het goed is gegaan zie je iets zoals dit.

```bash
Username (leave blank to use 'codespace'): *********
Email address: ****@*********.***
Password: 
Password (again): 
Superuser created successfully.
```

Op de sterretjes staan dan de zojuist ingevulde gegevens.

Start dan jouw site op. Vul dan achter de url /admin in. Log in met de zojuist aangemaakte account.

Klik dan op users, vervolgens kan je op iemands gebruikersnaam klikken om hun informatie te zien, je kan daar allerlei gegevens bewerken.


Als jij wilt dat je jouw site aleen kan zien als je bent ingelogd, ga dan naar /core/views.py, importeer dan deze libery.

```python
from django.contrib.auth.decorators import login_required # Importeer een module om inloggen verplicht te maken
```

Voor alle views die je wilt beveiligen met een login type dan deze regel boven de view.

```python
@login_required(login_url="login") # Verplicht het om in te loggen
```

Probeer die regel eens boven def index() te zetten. Als je nu naar jouw site gaat zal je zien dat je nog steeds op de hoofdpagina kan. Dat komt omdat je nog steeds bent ingelogd.

Nu zijn er 3 dingen die je kunt doen:
1. Verwijder je browsers cookies
2. Gebruik incognito mode
3. Maak een uitlog functie in jouw django site

Wij gaan natuurlijk voor 3. 

<h3>Uitloggen</h3>

Om een uitlog functie toe te voegen aan jouw site moet je eerst een url toevoegen, doe dat met de naam uitloggen.

Voeg dan deze uitlog functie toe aan /core/views.py.

```python
@login_required(login_url="login") # Verplicht login
def uitloggen(request): # View voor uitloggen
    auth.logout(request) # Loguit
    return redirect("login") # Ga naar de login pagina
```

Voeg daarboven ook de regel toe die zorgt dat je ingelogd moet zijn om bij die site te kunnen, want anders kan dat rare effecten hebben op jouw site.

Als je wilt kan je nu in jouw html code een knop toevoegen die mensen laat uitloggen, die code zou er dan ongeveer zo uitzien.

```html
<form action="/uitloggen" method="POST"> <!--Action is /uitloggen zodat als je op de submit knop drukt dat je daar naartoe gaat.-->
    {% csrf_token %} <!--Tegen csrf-->
    <button type="submit">Uitloggen</button> <!--Submit knop-->
</form>
```

<h3>Database algemeen</h3>

Je kan voor veel andere doeleinden ook een database gebruiken, hieronder ga je zien hoe jij zelf een database kan gebruiken voor jouw eigen idee.

Nu gaan wij als voorbeeld een paar blog posts laten zien.

Ga dan naar /core/models.py, Voeg deze code toe.

```python
class Post(models.Model): # Maakt een class genaamd post
    titel = models.CharField(max_length=200) # Veld voor de titel, met teken limiet
    inhoud = models.TextField() # Veld voor inhoud, zonder teken limiet
    gemaakt_op = models.DateTimeField(auto_now_add=True) # Veld voor datum (voegt automatisch toe)

    def __str__(self):
        return self.titel # Stuur de titel terug
```

Ga nu naar /core/admin.py en voeg daar dit toe.

```python
from .models import Post # Importeer het model

admin.site.register(Post) # Zorg dat je bij de database kan via het admin menu
```

Zodat je die database op jouw admin menu kan zien.

Migreer nu je aanpassingen door dit in je terminal te typen.

```bash 
python manage.py makemigrations
```

Om de veranderingen op te slaan, en:

```bash
python manage.py migrate
```

Om de veranderingen te updaten naar de database.

Start dan jouw site op en ga naar het admin menu, als het goed is zie je "core" staan en daaronder "Posts", druk dan op Post. Daar staat nog niets.

Maak nu een nieuw bestand aan genaamd post_list.html in de templates folder. Voeg daar deze html code toe.

```html
<h1>Blog Posts</h1> <!--Titel tekst boven lijst-->
<ul> <!--Ongesorteerde lijst-->
    {% for post in posts %} <!--Maak een link met django-->
        <li> <!--Lijst op volgorde-->
            {{ post.titel }}  <!--Laat de titel zien-->
            <br> <!--Een witregel-->
            {{ post.inhoud }} <!--Laat de inhoud zien-->
        </li>
    {% endfor %} <!--Einde link met django-->
</ul>
```

Ga dan naar /core/views.py en voeg daar deze functie toe.

```python
@login_required(login_url="login") # Verplicht login
def post_list(request): # Maak een view aan
    posts = Post.objects.all() # Importeer alle posts
    return render(request, 'post_list.html', {'posts': posts}) # Stuur html en posts naar de html
```

Ga dan naar /core/urls.py en maak een url aan naar deze view, zoals hieronder.

```python
    path('post_list', views.post_list, name='post_list'), # Maakt url aan
```

Start je website en ga naar de url. Als alles goed is gegaan zie je nog geen posts, die gaan we nu maken.

Ga naar je admin menu en druk dan onder "core" op "+ Add". Voeg een titel en inhoud toe, sla je post op en ga naar je site, dan die je de naam van de post en de inhoud.

