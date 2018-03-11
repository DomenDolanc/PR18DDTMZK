# Analiza filmov in napovedovanje njihove uspešnosti
Izberite vam zanimiv in dovolj kompleksen problem. Na kratko opišite problem ter navedite pomembnejše cilje oz. vprašanja, na katera boste skušali odgovoriti tekom analize podatkov.

Opišite vir in obliko podatkov.




# 1. Uvod
Področje naše raziskave bodo/so filmi. Zanima nas njihova uspešnost glede na igralce, režiserja, proračun in druge dejavnike.

Za problem smo si izbrali
# 2. Podatki
Viri podatkov: [The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset/data)
Podatki so v formatu CSV.
Zajemajo podatke o filmih, ključnih besedah, igralcih in preostankom ekipe.

### Podroben opis podatkov

### Filmi
-   `movies_metadata.csv` vsebuje podatke o filmih:

Atribut | Tip | Opis
-------- | -------- | --------
id  | Numeric | Identifikator
adult  |  Boolean | ?
belongs_to_collection   | String | Pripadajoča kolekcija
budget  | Numeric | Proračun namenjen izdelavi filma
genres  | String | Žanri
imdb_id | String | ID v sistemu imdb
original_language   | String | Originalen jezik
original_title  | String | Originalen naslov
overview    | String | Povzetek
popularity  | Numeric | Popularnost
production_companies    | String | Produkcijska podjetja
production_countries    | String | Produkcijske države
release_date    | DateTime | Datum izida
revenue | Numeric | Prihodki
runtime | Numeric | Dolžina
spoken_languages    | String | Jezik filma
status  | String | Stanje - ali je filem že izšel
title   | String | Naslov
video   | Boolean |
vote_average    | Numeric | Povprečje ocen
vote_count  | Numeric | Število ocen/glasov?

Atribut | Tip | Opis
-------- | -------- | --------
id | Numeric
cast | String
crew | String

Atribut | Tip | Opis
-------- | -------- | --------
id |Numeric |
keywords |String |