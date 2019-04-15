"""
    3.    Napisz program, który:
    a)    Zapyta się użytkownika pole jakiej figury chce policzyć (trójkąt, trapez, prostokąt, kwadrat)
    b)    Poprosi użytkownika o podanie niezbędnych danych do policzenia pola tej figury
    c)    Obliczy i wyświetli wynik użytkownikowi
    d)    Za pomocą elementów składni języka Python zabezpiecz program przed nieodpowiednim zachowaniem użytkownika
"""
# Funkcja sprawdzająca poprawność wprowadzonej liczby i zwracająca poprawnę liczbę
def SprawdzenieLiczby(tekst_zachety, komunikat_bledu, dolna_granica, gorna_granica):
    liczba = ''
    while not liczba.isdigit():
        liczba = input(tekst_zachety)
        if not liczba.isdigit():
            print(komunikat_bledu)
            liczba = ''
        elif not int(liczba) in range(dolna_granica, gorna_granica + 1):
            print(komunikat_bledu)
            liczba = ''
    return int(liczba)
def SprawdzenieLiczbyFl(tekst_zachety, komunikat_bledu):
    liczba = ''
    while not liczba.replace('.','',1).isdigit():
        liczba = input(tekst_zachety)
        if not liczba.replace('.','',1).isdigit():
            print(komunikat_bledu)
            liczba = ''
        else:
            return float(liczba)

def PoleTrojkata():
    a=SprawdzenieLiczbyFl("a= ", "Błędne dane")
    b=SprawdzenieLiczbyFl("b= ", "Błędne dane")
    c=SprawdzenieLiczbyFl("c= ", "Błędne dane")
    s = (a + b + c) / 2
    pole= (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print (str(pole))

def PoleTrapezu():
    a=SprawdzenieLiczbyFl("a= ", "Błędne dane")
    b=SprawdzenieLiczbyFl("b= ", "Błędne dane")
    h=SprawdzenieLiczbyFl("h= ", "Błędne dane")
    s = ((a + b) / 2)*h
    print (str(s))

def PoleKwadratu():
    a=SprawdzenieLiczbyFl("a= ", "Błędne dane")
    s = a * a
    print (str(s))

def PoleProstokata():
    a=SprawdzenieLiczbyFl("a= ", "Błędne dane")
    b=SprawdzenieLiczbyFl("b= ", "Błędne dane")
    s = a * b
    print (str(s))

pozycja_menu = 0
while pozycja_menu != 5:
    pozycja_menu = SprawdzenieLiczby('''
Program oblicza pola figur wybierz numer figury:
1 - Pole trójkąta
2 - Pole trapezu
3 - Pole prostokąta
4 - Pole kwadratu
5 - Koniec programu
Wybierz polecenie: ''', \
'To nie jest poprawne polecenie.\nWybierz jedną z dostępnych opcji 1 do 5', 1, 5)
    if pozycja_menu == 1:
        PoleTrojkata()
    elif pozycja_menu == 2:
       PoleTrapezu()
    elif pozycja_menu == 3:
        PoleProstokata()
    elif pozycja_menu == 4:
        PoleKwadratu()






