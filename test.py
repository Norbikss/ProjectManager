import pandas as pd
import numpy as np
from calendar import monthrange
from random import choice


def randomdays(num_days, num_workers):
	pracuje = []
	wybor = ["11-19", "Wolne"]
	for i in range(num_days):
		dzien = []
		for pracownik in num_workers:
			t_n = choice(wybor)
			dzien.append(t_n)

		pracuje.append(dzien)


	return pracuje

def godziny(lista, num_days, num_workers):
	godzin = []
	for i in range(num_workers):
		hours = 0
		for j in range(num_days):
			if lista[j][i] == "11-19":
				hours+=8
		godzin.append(hours)

	return godzin



num_days = monthrange(2022,6)[1]
days = pd.period_range(start='2022-06-01', end='2022-06-30', freq='D')
lista = ["Ania", "Hania", "Ewelina","Arek"]
b = randomdays(num_days, lista)
df = pd.DataFrame(index=[days], columns=lista, data = b)


c = godziny(b,num_days,len(lista))
df_new = pd.DataFrame([c], columns = lista, index=['Total'])
df = pd.concat([df, df_new])



df.to_excel("grafik.xlsx")
