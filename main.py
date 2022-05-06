import math as mt

def pole_figury(*args):
	if len(*args) < 4:
		for num in args:
			if len(*args) == 1:
				return mt.pi * num[0] ** 2
			elif len(*args) == 2:
				return num[0] * num[1]
			elif len(*args) == 3:
				p = (num[0] + num[1] + num[2]) / 2
				pole = mt.sqrt(p*(p-num[0])*(p-num[1])*(p-num[2]))
				return pole
		

liczba_figur = int(input())
lista_wartosci = []
wynik = 0

for l in range(liczba_figur):
	lista_wartosci = [float(x) for x in input().split()]
	try:
		wynik = wynik + pole_figury(lista_wartosci)
	except:
		wynik = False
		print("Błąd: można podać maksymalnie 3 liczby")
		break;

if wynik:
	print(round(wynik, 2))