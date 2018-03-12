# 1. Uvod
Področje naše raziskave so filmi. Zanima nas njihova uspešnost glede na igralce, režiserja, proračun in druge dejavnike.


# 2. Cilj raziskave
Analiza filmov in napovedovanje njihove uspešnosti.
Vizualno bomo predstavili rezultate naše raziskave v kateri bomo odgovorili na spodnja vprašanja:

- Kakšen je vpliv ekipe filma na njegovo uspešnost?
- Kaj vse vpliva na uspešnost filma?
- Analiza vložka in dobička glede na žanr.
- Analiza vložka in dobička glede na čas.

V sklopu naše raziskave bomo naredili aplikacijo, ki bo poizkušala napovedovati uspešnost filma.


# 3. Podatki
Viri podatkov: [The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset/data). Podatki so v  datoteki formata CSV.
Zajemajo podatke o filmih, ključnih besedah, igralcih in ekipi.



### Podroben opis podatkov

### Filmi
-   `movies_metadata.csv` vsebuje podatke o filmih:

Atribut | Tip | Opis
-------- | -------- | --------
id  | Numeric | Identifikacijski atribut
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
vote_average    | Numeric | Povprečje ocen
vote_count  | Numeric | Število ocen



### Sodelujoči
-   `credits.csv` vsebuje podatke o igralci in preostali ekipi:

Atribut | Tip | Opis
-------- | -------- | --------
id | Numeric | Identifikacijski atribut
cast | String | Seznam igralcev
crew | String | Seznam ljudi v ekipi


### Ključne besede
-   `credits.csv` vsebuje podatke o ključnih besedah za določen film:

Atribut | Tip | Opis
-------- | -------- | --------
id | Numeric | Identifikacijski atribut
keywords |String | Ključne besede