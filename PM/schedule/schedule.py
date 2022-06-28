import pandas as pd
import numpy as np
from datetime import date
from calendar import monthrange
from random import choice
from .models import Profile, Employee, Vacation, Free_days, Work_day
from django.contrib.auth.models import User, auth

class Schedule_generator:

	def __init__(self, employer, employee, start_date, end_date):
		self.employer = employer
		self.employee = employee
		self.start_date = start_date
		self.end_date = end_date
		self.holiday = ['01-01-2022','06-01-2022','17-04-2022','18-04-2022', '01-05-2022', '03-05-2022', 
					'16-06-2022', '15-08-2022', '01-11-2022', '11-11-2022', '25-12-2022', '26-12-2022']


	def all_days(self):
		days = pd.period_range(start=self.start_date, end=self.end_date, freq='D')
		return days

	def is_str_date(self, day):
		return day.strftime('%d-%m-%Y')

	def is_str_date2(self, day):
		return day.strftime('%Y-%m-%d')



	def weekday(self):
		all_days = self.all_days()
		name_days = []
		dzien = {
			'0': 'Poniedziałek',
			'1': 'Wtorek',
			'2': 'Środa',
			'3': 'Czwartek',
			'4': 'Piątek',
			'5': 'Sobota',
			'6': 'Niedziela'
		}
		for day in all_days:
			today = str(day.day_of_week)
			if self.is_str_date(day) in self.holiday:
				name_days.append('Swieto')	
			else:
				name_days.append(dzien[today])
		return name_days


	def total_hours(self):
		total_hours = 0
		for day in self.weekday():
			if day == "Sobota" or day == "Niedziela" or day == "Swieto":
				continue
			else:
				total_hours += 8

		return total_hours

	def main(self):
		#pracuje = []
		day = self.all_days()
		days = self.weekday()
		wybor = ["9-21", "Wolne"]
		for i in range(len(self.weekday())):
			if days[i] == "Sobota" or days == "Niedziela" or days == "Swieto":
				work_day = Work_day.objects.create(employer = self.employer, employee = self.employee, day = self.is_str_date2(day[i]),time = "W", worked_hours = 0 )
				work_day.save()
				#pracuje.append("Wolne")
			else:
				t_n = choice(wybor)
				if t_n == "Wolne":
					work_day = Work_day.objects.create(employer = self.employer, employee = self.employee, day = self.is_str_date2(day[i]),time = "W", worked_hours = 0 )
					work_day.save()
				else:
					work_day = Work_day.objects.create(employer = self.employer, employee = self.employee, day = self.is_str_date2(day[i]),time = "G", worked_hours = 12 )
					work_day.save()
		


	