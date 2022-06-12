import pandas as pd
import numpy as np
from datetime import date
from calendar import monthrange
from random import choice


class Kalendarz:

	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day
		self.num_days = monthrange(self.year,self.month)[self.day]
	#def weekday(self,dzienn):
		#dzien = {
			#'1': 'Poniedziałek',
			#'2': 'Wtorek',
			#'3': 'Środa',
			#'4': 'Czwartek',
			#'5': 'Piątek',
			#'6': 'Sobota',
			#'7': 'Niedziela'
		#}
		#nazwa = str(date(self.year,self.month,dzienn).isoweekday())
		#return dzien[nazwa]



	def weekday(self):
		days = []
		#day = 1
		dzien = {
			'1': 'Poniedziałek',
			'2': 'Wtorek',
			'3': 'Środa',
			'4': 'Czwartek',
			'5': 'Piątek',
			'6': 'Sobota',
			'7': 'Niedziela'
		}
		for i in range(self.num_days):
			czas = str(date(self.year,self.month,i+1).isoweekday())
			days.append(dzien[czas])
			
		return days

b = Kalendarz(2022,6,1)

print(b.weekday())