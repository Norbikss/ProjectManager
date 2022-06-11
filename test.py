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
			if pracownik != "TOTAL":
				t_n = choice(wybor)
				dzien.append(t_n)
			else:
				godziny = 0
				for day in dzien:
					if day == "11-19":
						godziny += 8
				dzien.append(godziny)
		pracuje.append(dzien)


	return pracuje

num_days = monthrange(2022,6)[1]
days = pd.period_range(start='2022-06-01', end='2022-06-30', freq='D')
lista = ["Ania", "Hania", "Ewelina","Arek","TOTAL"]
b = randomdays(num_days, lista)
df = pd.DataFrame(index=days, columns=lista, data = b)
df.to_excel("grafik.xlsx")