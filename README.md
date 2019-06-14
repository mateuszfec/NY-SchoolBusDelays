## School bus delays in New York - Data analysis (clustering) [PL]

##### Akademia Górniczo Hutnicza im. Stanisława Staszica w Krakowie <br> Wydział Zarządzania, Informatyka i Ekonometria, Uczenie maszynowe
###### Prowadzący: dr inż. Maciej Wielgosz, dr inż. Marcin Pietroń <br> Opracowanie: Mateusz Feć, Patryk Zieliński, Kraków 2019

## Wprowadzenie
Celem projektu jest wykorzystanie metod analizy skupień do przeanalizowania powodów, przyczyn oraz efektów opóźnień autobusów szkolnych w Nowm Jorku. Dane pochodzą z serwisu [Kaggle](https://www.kaggle.com/new-york-city/ny-bus-breakdown-and-delays) na licencji [CCO public domain](https://creativecommons.org/share-your-work/public-domain/cc0/). Szczegółowy opis danych znajduje się poniżej.

## Opis danych
1. **Zmienne kategoryczne**
    * Delay_Reason - zmienna kategoryczna przyjmująca wartości **1-10** w zależności od rozpoznanych przyczyn awarii,tj.:
        * 1 - przyczyna nierozpoznana/nie została zgłoszona
        * 2 - wypadek
        * 3 - opóźnienie przez szkołę
        * 4 - przebita opona
        * 5 - wysokie natężenie ruchu
        * 6 - późny powrót z wycieczki
        * 7 - usterka mechaniczna
        * 8 - inne
        * 9 - problem z wyjazdem
        * 10 - warunki pogodowe
        * 11 - brak możliwości uruchomienia zapłonu
    * School_Year - rok szkolny
        * 1 - 2015/16
        * 2 - 2016/17
        * 3 - 2017/18
        * 4 - 2018/19
    * School_Level - jeden z dwóch poziomów edukacji
        * 1 - wiek przedszkolny
        * 2 - wiek szkolny
    * Delay_Result - skutki opóźnienia
        * 1 - awaria
        * 2 - opóźniony przyjazd
    * Bus_Company - jedna z 62 firm transportowych świadczących usługi przewozowe dla szkół
    * Boro - jedna z 10 dzielnic Nowego Jorku (wartości **2-10** oraz **12**); wartość **11** przyjęto dla nierozpoznanej dzielnicy
        * 1 - wszystkie dzielnice
        * 2 - Bronx
        * 3 - Brooklyn
        * 4 - Connecticut
        * 5 - Manhattan
        * 6 - Nassau County
        * 7 - New Jersey
        * 8 - Queens
        * 9 - Rockland County
        * 10 - Staten Island
        * 11 - brak danych
        * 12 - Westchester
    * Route_Number - unikalny identyfikator trasy autobusu szkolnego
    * Bus_Number - unikalny identyfikator autobusu szkolnego
    * Bus_Run_Type - rodzaj przewozu
        * 1 - nieznany
        * 2 - General Ed AM Run
        * 3 - General Ed Field Trip
        * 4 - General Ed PM Run
        * 5 - Pre-K/EI
        * 6 - Project Read AM Run
        * 7 - Project Read Field Trip
        * 8 - Project Read PM Run
        * 9 - Special Ed AM Run
        * 10 - Special Ed Field Trip
        * 11 - Special Ed PM Run
    * OPT_Alerted - zmienna binarna
        * 1 - w systemie zarejestrowano opóźnienie autobusu
        * 0 - inaczej
    * Schools_Notified - zmienna binarna
        * 1 - szkoła została poinformowana o opóźnieniu autobusu
        * 0 - inaczej
    * Parents_Notified - zmienna binarna 
        * 1 - rodzice poinformowani o opóźnieniu autobusu
        * 0 - inaczej

2. **Zmienne ciągłe**
    * Bus_Delay - czas opóźnienia autobusu
    * Event_Date - data wystąpienia opóźnienia
    * Occurred_On - czas wystąpienia opóźnienia
    * Informed_On - czas poinformowania pasażerów o opóźnieniu
    * Reaction_Time - czas reakcji liczony jako czas pomiędzy czasem wystąpienia opóźnienia a czasem poinformowania pasażerów
    * Students_Number - liczba uczniów znajdujących się w autobusie w momencie wystąpienia opóźnienia
## Hipotezy badawcze
[comment]: <> (todo)

## Stosowane algorytmy
1. [Metoda k-średnich](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
2. [MeanShift](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html)

[comment]: <> (todo: zastanowic sie nad finalnie uzywanymi metodami)
## Analiza działania algorytmów
Poniższa tabela przedstawia analizę porównawczą czasów wykonywania badanych algorytmów klasteryzacji w zależności od wielkości próbki danych.*

| Algorytm             | Sample 10%    |  Sample 25% | Sample 50% | Sample 75% | Sample 100% |
|----------------------|:-------------:|------------:|-----------:|-----------:|------------:|
| Metoda k-średnich    |    1.5s       |   4.7s      |   12.4s    |   20.9s    |   xx.xxs    |
| MeanShift            |    1.3s       |   3.1s      |    5.6s    |   9.5s     |   xx.xxs    |

Poniższa tabela przedstawia analizę porównawczą liczby klastrów jakie zostały wyodrębnione przez poszczególne algorytmy w zależności od wielkości próbki danych.*

| Algorytm             | Sample 10%    |  Sample 25% | Sample 50% | Sample 75% | Sample 100% |
|----------------------|:-------------:|------------:|-----------:|-----------:|------------:|
| Metoda k-średnich    |    3          |   3         |   3        |       3    |   3         |
| MeanShift            |    11         |   18        |       20   |   23       |       xx    |

*Wszystkie wartości czasowe oraz liczbowe zostały uzyskane na jednolitym środowisku testowym o architekturze 64-bitowej.

[comment]: <> (todo: Wykresy/ploty w jakimś dobrym ułożeniu)

## Otrzymane wyniki

[comment]: <> (todo: analiza 2 przypadkow "uzycia")

## Podsumowanie 
[comment]: <> (todo)



