
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

Als het goed is zie je dan 2 folders, 1 python bestand en database bestand. 

Open de map met "mijnProjectNaam". Dan heb je 1 folder en 6 python bestanden.

Open het bestand "views.py".
