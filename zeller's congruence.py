# Zeller's congruence

try:
	d = int(input('Podaj dzien tygodnia \n'))
	month = int(input("Podaj dzien miesiaca (Styczen jako 13 i luty jako 14) \n"))
	year = int(input('Podaj rok \n')) 
	
except ValueError:
	print('podaj inta a nie stringa')
J = year // 100
days_of_the_week = ['Sobota', 'Niedziela', 'Poniedzialek', 'Wtorek', 'Sroda', 'Czwartek', 'Piatek']

# wzor dla kalendarza gregorianskiego 
def GregorianCalendar(d, month, year):
	global day_of_the_week
	day_of_the_week = (d +((13 * (month+1))// 5) + year + (year // 4) + (J // 4) + 5 * J) % 7
	return day_of_the_week
# wzor dla kalendarza julianskiego
def JulianCalendar(d, month, year):
	day_of_the_week_2 = (d +((13 * (month+1))// 5) + year + (year // 4) + 5 + 6 * J) % 7
	return day_of_the_week_2

if year > 1582:
	year = year % 100
	GregorianCalendar(d, month, year)
	print(days_of_the_week[day_of_the_week])
else:
	year = year % 100 
	print(days_of_the_week[JulianCalendar(d, month, year)])