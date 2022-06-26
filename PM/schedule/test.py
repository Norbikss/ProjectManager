import pandas as pd
import numpy as np
from datetime import date
from calendar import monthrange
from random import choice
from .models import Profile, Employee, Vacation, Free_days

class Schedule_generator:

	def __init__(self, year, month, day,num_days,workers):
		self.year = year
		self.month = month
		self.day = day 
		self.num_days = num_days
		self.workers = workers

	def weekday(year,month,day,num_days):
		days = []
		dzien = {
			'1': 'Poniedziałek',
			'2': 'Wtorek',
			'3': 'Środa',
			'4': 'Czwartek',
			'5': 'Piątek',
			'6': 'Sobota',
			'7': 'Niedziela'
		}
		for i in range(num_days):
			czas = str(date(year,month,day).isoweekday())
			days.append(dzien[czas])
			day += 1
		return days


	def randomdays(num_days, num_workers, weekday):
		pracuje = []
		wybor = ["11-19", "Wolne"]
		for i in range(num_days):
			dzien = []
			for pracownik in num_workers:
				if weekday[i] == 'Sobota' or weekday[i] == 'Niedziela':
					dzien.append("Wolne")
				else:
					t_n = '9-21'
					dzien.append(t_n)

			pracuje.append(dzien)


		return pracuje

	def godziny(lista, num_days, num_workers):
		godzin = []
		for i in range(num_workers):
			hours = 0
			for j in range(num_days):
				if lista[j][i] == "9-21":
					hours+=12
			godzin.append(hours)

		return godzin



num_days = monthrange(2022,6)[1]
#days = pd.period_range(start='2022-06-01', end='2022-06-30', freq='D')
dni_tygodnia = weekday(2022,6,1,num_days)
lista = ["Ania", "Hania", "Ewelina","Arek"]
b = randomdays(num_days, lista, dni_tygodnia)
df = pd.DataFrame(index=[dni_tygodnia], columns=lista, data = b)


c = godziny(b,num_days,len(lista))
df_new = pd.DataFrame([c], columns = lista, index=['Total'])
df = pd.concat([df, df_new])


df.to_excel('grafik.xlsx')