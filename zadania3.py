# 1
user_role = "admin"
is_logged = True

if user_role == "admin" and is_logged:
    print('Witaj w panelu admina')
elif user_role == "mod" and is_logged:
    print('Witaj w panelu moderatora')
else:
    print('Błąd logowania')

#2
user_country = "Polska"

if user_country == "Polska" or user_country == "Czechy" or user_country == "Niemcy":
    print('Witaj w panelu zamówień')
else:
    print('Dostawa towaru niemożliwa')

#3
from datetime import datetime
godzina = datetime.now()

print(godzina.hour)
if godzina.hour > 6 and godzina.hour < 12:
    print("Good Morning")
elif godzina.hour > 12 and godzina.hour < 18:
    print("Good Afternoon")
else:
     print("Good Evening")

