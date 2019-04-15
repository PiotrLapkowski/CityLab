#Lista 01. Zadanie 1
#1.    Napisz program, który:
#a)    Pobierze od użytkownika jego datę urodzenia (format dd-mm-yyyy), następnie na tej podstawie określi jego wiek, oraz w jaki dzień tygodnia przypadają jego urodziny w tym roku oraz za 15 lat.
#b)    Wyświetli użytkownikowi komunikat „Witaj, masz X lat, w tym roku Twoje urodziny wypadają w [dzień tygodnia], za 15 lat będziesz świętować w [dzień tygodnia urodzin za 15 lat]”.
#c)    Za pomocą elementów składni języka Python zabezpiecz program przed nieodpowiednim zachowaniem użytkownika

# ******** FUNKCJE ********

# Funkcja sprawdzająca poprawność wprowadzonej daty i zwracająca datę w formacie dd-mm-yyyy
def SprawdzenieDaty (tekst_zachety):
    import datetime
    dataU=input(tekst_zachety)
    try:
        dataU = datetime.datetime.strptime(dataU, "%d-%m-%Y")
        return dataU 
    except ValueError:
        print ("Blad daty")   
def DzienPL (ag):
    #zwraca dzień tygodnia po polsku
    if ag==0:
        return "Poniedziałek"
    elif ag==1:
        return "Wtorek"
    elif ag==2:
        return "Środa"
    elif ag==3:
        return"Czwartek"
    elif ag==4:
        return"Piątek"
    elif ag==5:
        return"Sobota"
    elif ag==6:
        return"Niedziela"

  

   


# ******** Program glowny ********#
import calendar, datetime

data = SprawdzenieDaty( "Podaj datę urodzenia w formacie dd-mm-rrrr: " )
#data_rob = '12-06-1965'
#data = datetime.datetime.strptime(data_rob,  "%d-%m-%Y")
d =data.day
m =data.month
today2 = data.today()
y= today2.year
Teraz = datetime.date(y, m, d)
Przyszlosc = datetime.date(y+15, m, d)
#day=calendar.day_name[data.weekday()]
day=DzienPL(data.weekday())
print ("Twoja data urodzin " + str(data) + " dzień urodzin to " +str(day))
#data urodzin w tym roku
#day=calendar.day_name[Teraz.weekday()]
day=DzienPL(Teraz.weekday())
print ("W tym roku urodziny wypadają w: " + str(day))
#data urodzin za 15 lat
#day= calendar.day_name[Przyszlosc.weekday()]
day=DzienPL(Przyszlosc.weekday())
print ("Urodziny w " + str(Przyszlosc) + " wypadają w "+  str(day))



