#Lista 01. Zadanie 1
#1.    Napisz program, który:
#a)    Pobierze od użytkownika jego datę urodzenia (format dd-mm-yyyy), następnie na tej podstawie określi jego wiek, oraz w jaki dzień tygodnia przypadają jego urodziny w tym roku oraz za 15 lat.
#b)    Wyświetli użytkownikowi komunikat „Witaj, masz X lat, w tym roku Twoje urodziny wypadają w [dzień tygodnia], za 15 lat będziesz świętować w [dzień tygodnia urodzin za 15 lat]”.
#c)    Za pomocą elementów składni języka Python zabezpiecz program przed nieodpowiednim zachowaniem użytkownika

# ******** FUNKCJE ********

# Funkcja sprawdzająca poprawność wprowadzonej daty i zwracająca datę w formacie dd-mm-yyyy
def SprawdzenieDaty (tekst_zachety):
    import datetime
    data_=input(tekst_zachety)
    data_ = datetime.datetime.strptime(data_, "%d-%m-%Y")
    return data_

def SprawdzenieDaty2(tekst_zachety):
    import datetime
    data_u = '01-01-1900'
    while data_u != datetime.datetime.strptime(data_u, "%d-%m-%Y"):
        data_u = input(tekst_zachety)
        data_u =datetime.datetime.strptime(data_u, "%d-%m-%Y")        
    return data_u

   


# ******** Program glowny ********#
import calendar, datetime
#data = SprawdzenieDaty( "Podaj datę urodzenia: ")
data_rob = '12-06-1965'
data = datetime.datetime.strptime(data_rob,  "%d-%m-%Y")
d =data.day
m =data.month
today2 = data.today()
y= today2.year
Teraz = datetime.date(y, m, d)
Przyszlosc = datetime.date(y+15, m, d)
day=calendar.day_name[data.weekday()]
print ("Twoja data urodzin " + str(data) + " dzień urodzin to " +str(day))
#data urodzin w tym roku
day=calendar.day_name[Teraz.weekday()]
print ("W tym roku urodziny wypadają w: " + str(day))
#data urodzin za 15 lat
day= calendar.day_name[Przyszlosc.weekday()]
print ("Urodziny w " + str(Przyszlosc) + " wypadają w "+  str(day))


