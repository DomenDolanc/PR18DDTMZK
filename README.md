# Sodelujoči
- [Domen Dolanc](https://github.com/DomenDolanc)
- [Tomaž Martinčič](https://github.com/tm1897)
- [Žiga Klopčič](https://github.com/klopcic)

# Povezave
- [Osnutek](osnutek.md)
- [Aplikacija prikaz žanrov na zemljevidu skozi čas](map.html)


------------------

# Cilj raziskave
Analiza filmov in napovedovanje njihove uspešnosti.
Vizualno bomo predstavili rezultate naše raziskave v kateri bomo odgovorili na spodnja vprašanja:

- Kaj vse vpliva na uspešnost filma?
- Analiza vložka in dobička glede na žanr.
- Analiza vložka in dobička glede na čas.

Pripravili bomo animacijo, ki bo prikazovala popularnost žanrov na zemljevidu skozi čas.

#### Uporabljene knjižnice

- Orange
- collections
- matplotlib
- numpy
- json
- pandas
- dateutil
- EasyMoney


Na spodnji sliki je prikazana korelacija med prihodkom in številom ocen.

![png](readme_images/output_4_0.png)

Spodnja slika prikazuje proračun in prihodki za posamezen žanr.

![png](readme_images/output_6_0.png)


Spodnja slika prikazuje število filmov prikazanega žanra skozi leta.

![png](readme_images/output_8_0.png)

Število filmov posameznega žanra v obdobju 2. svetovne vojne.

![png](readme_images/output_9_0.png)

Spodnji sliki prikazujeta vsoto in povprečje prihodkov skozi čas.

![png](readme_images/output_10_0.png)

Zemljevid, ki prikazuje njabolj snemane žanre v državi za vsako leto:
![gif](readme_images/map.gif)
Druge hitrosti:

- [0.2s zamik](readme_images/map-0.2s-delay.gif)
- [2s zamik](readme_images/map-2s-delay.gif)