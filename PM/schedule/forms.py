from django import forms
from django.forms import ModelForm
from .models import Employee, Work_day
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm, PasswordChangeForm


class EmployeeForm(ModelForm):
	class Meta:
		model = Employee
		fields = ("name", "surname","position","work_time")

class PasswordChange(PasswordChangeForm):
    pass

class EmailChange(ModelForm):
	class Meta:
		model = User
		fields = ['email']
class PickEmployee(forms.Form):
	
	choices = forms.MultipleChoiceField(
		widget = forms.CheckboxSelectMultiple
		)