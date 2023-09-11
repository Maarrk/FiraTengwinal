# FiraTengwinal

Font do używania [Tengwaru](https://pl.wikipedia.org/wiki/Tengwar) w terminalu

## Instalacja

Gotowy plik TTF jest dostępny do pobrania w sekcji `Releases`

## Modyfikowanie fontu

- Projekt znaków jest w pliku `glify.svg`
- Zalecany Linux (problemy z Inkscape w wierszu poleceń windows)
- Wymagania
  - Python 3
  - Inkscape 1.2+ (wiele stron)
  - FontForge 2020-03-14+ (skrypty Python)
- Skopiuj `glify.svg` do `/tmp`
- Otwórz [Fira Code](https://github.com/tonsky/FiraCode) lub [jej wersję z dodatkowymi ikonami](https://www.nerdfonts.com/font-downloads) w FontForge
- Kliknij `Plik` -> `Wykonaj skrypt`, lub Ctrl+.
- Wklej zawartość `ff_replace.py` do pola tekstowego i kliknij `OK`
- Poczekaj aż wszystkie litery zostaną podmienione

## Wykorzystane źródła

- [Tengwar dla języka polskiego](http://www.mimas.ceti.pl/tengwar/jezyk-polski.php), wykorzystany z drobnymi zmianami
- [Fira Mono](https://github.com/mozilla/Fira), oryginalny projekt użytego fontu
- [Fira Code](https://github.com/tonsky/FiraCode), ligatury dla programowania
