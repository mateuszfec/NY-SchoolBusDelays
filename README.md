## School bus delays in New York - Data analysis (clustering) [PL]

##### Akademia Górniczo Hutnicza im. Stanisława Staszica w Krakowie <br> Wydział Zarządzania, Informatyka i Ekonometria, Uczenie maszynowe
###### Prowadzący: dr inż. Maciej Wielgosz, dr inż. Marcin Pietroń <br> Opracowanie: Mateusz Feć, Patryk Zieliński, Kraków 2019

## Wprowadzenie
Celem projektu jest wykorzystanie metod analizy skupień do przeanalizowania powodów, przyczyn oraz efektów opóźnień autobusów szkolnych w Nowm Jorku. Dane pochodzą z serwisu [Kaggle](https://www.kaggle.com/new-york-city/ny-bus-breakdown-and-delays) na licencji [CCO public domain](https://creativecommons.org/share-your-work/public-domain/cc0/). Szczegółowy opis danych znajduje się poniżej.

## Opis danych
1. **Zmienne kategoryczne**
    * Delay_Reason - zmienna kategoryczna przyjmująca wartość **1** w sytuacji, gdy nie wystąpiło opóźnienie oraz wartości **2-11** w zależności od rozpoznanych przyczyn awarii,tj.:
        wypadek, korek, usterka mechaniczna, warunki pogodowe, brak możliwości uruchomienia zapłonu itp.
    * School_Year
    * School_Level - jeden z dwóch poziomów edukacji (**1** - wiek przedszkolny, **2** - wiek szkolny)
    * Delay_Result - dwa skutki opóźnienia - awaria (wartość **1**) oraz opóźniony przyjaxd (wartość **2**)
    * Bus_Company - jedna z 62 firm transportowych świadczących usługi przewozowe dla szkół
    * Boro - jedna z 10 dzielnic Nowego Jorku (wartości **2-10** oraz **12**); wartość **11** przyjęto dla nierozpoznanej dzielnicy
    * Route_Number - unikalny identyfikator trasy autobusu szkolnego
    * Bus_Number - unikalny identyfikator autobusu szkolnego
    * Bus_Run_Type
    * OPT_Alerted
    * Schools_Notified - zmienna binarna przyjmująca wartość **1** w sytuacji, gdy szkoła został poinformowana o opóźnieniu autobusu oraz **0** w pozostałych przypadkach
    * Parents_Notified - zmienna binarna przyjmująca wartość **1** w sytuacji, gdy rodzice zostali poinformowani o opóźnieniu autobusu oraz **0** w pozostałych przypadkach
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
2. [Affinity propagation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html)
3. [MeanShift](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html)

[comment]: <> (todo: zastanowic sie nad finalnie uzywanymi metodami)
## Otrzymane wyniki
Poniższa tabela przedstawia analizę porównawczą czasów wykonywania badanych algorytmów klasteryzacji w zależności od wielkości próbki danych.*

| Algorytm             | Sample 10%    |  Sample 25% | Sample 50% | Sample 75% | Sample 100% |
|----------------------|:-------------:|------------:|-----------:|-----------:|------------:|
| Metoda k-średnich    |    xx.xxs     |   xx.xxs    |   xx.xxs   |   xx.xxs   |   xx.xxs    |
| Affinity propagation |    xx.xxs     |   xx.xxs    |   xx.xxs   |   xx.xxs   |   xx.xxs    |
| MeanShift            |    xx.xxs     |   xx.xxs    |   xx.xxs   |   xx.xxs   |   xx.xxs    |

Poniższa tabela przedstawia analizę porównawczą liczby klastrów jakie zostały wyodrębnione przez poszczególne algorytmy w zależności od wielkości próbki danych.*

| Algorytm             | Sample 10%    |  Sample 25% | Sample 50% | Sample 75% | Sample 100% |
|----------------------|:-------------:|------------:|-----------:|-----------:|------------:|
| Metoda k-średnich    |    xx         |   xx        |   xx       |       xx   |   xx        |
| Affinity propagation |    xx         |   xx        |   xx       |   xx       |   xx        |
| MeanShift            |    xx         |   xx        |       xx   |   xx       |       xx    |

*Wszystkie wartości czasowe oraz liczbowe zostały uzyskane na jednolitym środowisku testowym o architekturze 64-bitowej.

[comment]: <> (todo: Wykresy/ploty w jakimś dobrym ułożeniu)

## Podsumowanie 
[comment]: <> (todo)



