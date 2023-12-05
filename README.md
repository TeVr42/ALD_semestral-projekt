# ALD Semestrální práce
*Autor: Tereza Vrbová*

## Základní fungování
Tato aplikace generuje herní mapu.
Na hlavní stránce je možné zvolit si rozměry (maximálně 99x99) a typ mapy (3 různé druhy dlaždic) a zvolit generování.
Následně se vygeneruje mapa.
Kliknutím na navigační lištu je možný návrat na hlavní stránku a nové generování.

## Spuštění
Aplikace využívá framework Flask, ke spuštění (Windows) proto doporučuji následující:
```
$env:FLASK_APP = "main.py"
flask run
```
A pak už jen rozkliknout link...

## Podstata generování
Při volbě mapy se načtou dlaždice ze složky s obrázky. Každý takový obrázek se uloží do úložiště dlaždic 4x - nejen ve své původní podobě, ale také pootočený o 90, 180 a 270 stupňů, tím se rozšiřuje množství možných umístěných dlaždic.

Generování začíná náhodným výběrem počáteční dlaždice. 

Následující dlaždice je vybírána opět náhodně, ale již z omezené množiny. Na základě omezení vyplývajících z předchozích dlaždic (musí se shodovat znak identifikující pravý okraj předchozí draždice s levým nové, popřípadě dolní dlaždice nad umísťovanou a horní okraj nové) se vytvoří list možných dlaždic a z nich se náhodně vybere dlaždice.

Pokud nelze umístit na toto místo žádnou dlaždici, program se o krok vrátí a umístí předchozí dlaždici znova. Také si uchovává informace kolikrát jakou dlaždici umísťoval (kolikrát se k ní vracel). Pokud se k nějaké vrací opakovaně, je pravděpodobně zaseknutý ve smyčce,  vrátí se tedy ještě o 1 a vymaže informace o umísťování následujících dlaždic, tím smyšku přeruší.

Informace o dlaždicích jsou uchovány v názvu, program je tedy snadno upravovatelný pro vlastní sadu dlaždic - stačí zachovat pojmenování, a to stejná písmena pro navazující motiv (př. kraj s vodou vždy uchován jako V), po směru hodinových ručiček, počínaje horním okrajem (dlaždice s vodou nahoře, hradem dole a cestou vlevo a vpravo - VCHC).

## Závěrem
Veselé generování!
