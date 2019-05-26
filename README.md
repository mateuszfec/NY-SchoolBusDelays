## Akademia Górniczo Hutnicza im. Stanisława Staszica w Krakowie
## Wydział Zarządzania
## Kierunek: Informatyka i Ekonometria
## Uczenie maszynowe - projekt zaliczeniowy
## Temat:  School bus delays in New York - Data analysis (clustering)
## Prowadzący: dr inż. Maciej Wielgosz, dr inż. Marcin Pietroń
## Opracowali: Mateusz Feć, Patryk Zieliński
### Kraków 2019

## Wprowadzenie i opis danych
Celem projektu jest wykorzystanie metod analizy skupień do przeanalizowania opóźnień autobusów szkolnych w Nowym Jorku. (**COŚ TU JESZCZE MOŻNA DODAĆ**)
## Opis danych
1. Zmienne kategoryczne
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
2. Zmienne ciągłe
    * Bus_Delay - czas opóźnienia autobusu
    * Event_Date - data wystąpienia opóźnienia
    * Occurred_On - czas wystąpienia opóźnienia
    * Informed_On - czas poinformowania pasażerów o opóźnieniu
    * Reaction_Time - czas reakcji liczony jako czas pomiędzy czasem wystąpienia opóźnienia a czasem poinformowania pasażerów
    * Students_Number - liczba uczniów znajdujących się w autobusie w momencie wystąpienia opóźnienia
## Hipotezy badawcze (? - najlepiej to na samym końcu dać pod warunkiem że chcemy)
## Stosowane metody
1. Metoda k-średnich
2. Affinity propagation (czy zmieniamy ?)
## Otrzymane wyniki
## Podsumowanie 



