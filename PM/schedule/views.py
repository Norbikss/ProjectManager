from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm, PasswordChangeForm
from .models import Profile, Employee, Vacation, Free_days
from .forms import EmployeeForm, PasswordChange, EmailChange
#form .schedule import Schedule

# Create your views here.
@login_required(login_url = 'login')
def index(request):
	user = User.objects.get(username = request.user)
	return render(request, 'index.html', {'user': user})

def login(request):

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username = username, password = password)

		if user is not  None:
			auth.login(request, user)
			return redirect('index')
		else:
			messages.info(request, "Username or password incorrect!")
	return render(request, 'login.html')

def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password2 = request.POST['password2']

		if password == password2:
			if User.objects.filter(email=email).exists():
				messages.info(request, 'Email Taken')
				return redirect('register')
			elif User.objects.filter(username=username).exists():
				messages.info(request, 'Username Taken')
				return redirect('register')
			else:
				user = User.objects.create_user(username = username, email = email, password = password)
				user.save()

				user_login = auth.authenticate(username=username, password=password)
				auth.login(request, user_login)

				user_model = User.objects.get(username = username)
				new_profile = Profile.objects.create(user = user_model)
				new_profile.save()
				return redirect('index')
		else:
			messages.info(request, 'Password Not Matching')
			return redirect('register')
	return render(request, 'register.html')

@login_required(login_url = 'login')
def add_employee(request):
	user = request.user
	employer = Profile.objects.get(user = user)

	if request.method == "POST":
		name = request.POST['name']
		surname = request.POST['surname']
		position = request.POST['position']
		etat = request.POST['etat']

		employee = Employee(employer = employer, name = name, surname = surname, position = position, work_time = etat)
		employee.save()
		return redirect('show_employees')

	return render(request, 'add_employee.html')
@login_required(login_url = 'login')
def show_employees(request):
	user = request.user
	employer = Profile.objects.get(user = user)
	employer_employee = Employee.objects.filter(employer = employer)
	employee_list = []
	for employee in employer_employee:
		employee_list.append(employee)



	return render(request, 'show_employees.html', {'employees': employee_list})

@login_required(login_url = 'login')
def emp_profile(request, pk):
	employee = get_object_or_404(Employee, id = pk)
	vacations = Vacation.objects.filter(employee = employee)
	free_days = Free_days.objects.filter(employee = employee)

	return render(request, 'profile.html', {'employee': employee, 'free_days': free_days, "vacations": vacations})

@login_required(login_url = 'login')
def free_days(request):
	user = request.user
	employer = Profile.objects.get(user = user)
	employer_employee = Employee.objects.filter(employer = employer)
	employee_list = []
	for employee in employer_employee:
		employee_list.append(employee)

	if request.method == "POST":
		employee = request.POST['employee']
		the_employee = Employee.objects.get(id = employee)
		free_day_type = request.POST['free_day_type']
		if free_day_type == "vacation":
			start_date = request.POST['start_date']
			end_date = request.POST['end_date']

			vacation = Vacation(employee = the_employee,start_date = start_date, end_date = end_date)
			vacation.save()
		elif free_day_type == 'free_day':
			free_day = request.POST['start_date']
			free_day = Free_days(employee = the_employee, date = free_day)
			free_day.save()

			

	return render(request, 'free_days.html', {'employees': employee_list})


@login_required(login_url = 'login')
def create_schedule(request):
	user = request.user
	employer = Profile.objects.get(user = user)
	employer_employee = Employee.objects.filter(employer = employer)
	employee_list = []
	for employee in employer_employee:
		employee_list.append(employee)
	if request.method == "POST":
		for_who = request.POST['employee']
		start_date = request.POST['start_date']
		end_date = request.POST['end_date']
		# for employee in for_who:
			#personal = Schedule(employee, start_date, end_date)
		
		

	return render(request, 'create_schedule.html',{'employees': employee_list})
@login_required(login_url = 'login')
def edit_employee(request, employee_id):
	employee = Employee.objects.get(id = employee_id)
	form = EmployeeForm(request.POST or None, instance = employee)
	if form.is_valid():
		form.save()
		return redirect('show_employees')
	return render(request, 'edit_employee.html',{'form': form, "employee": employee})
@login_required(login_url = 'login')
def delete_employee(request, employee_id):
	employee = Employee.objects.get(id = employee_id)
	employee.delete()
	return redirect('show_employees')
@login_required(login_url = 'login')
def delete_vacation(request, pk):
	vacation = Vacation.objects.get(id = pk)
	employee = Employee.objects.get(id = free_day.employee.id)

	vacation.delete()
	return redirect('emp_profile', pk = employee.id)
@login_required(login_url = 'login')	
def delete_free_day(request, pk):

	free_day = Free_days.objects.get(id = pk)

	employee = Employee.objects.get(id = free_day.employee.id)
	
	free_day.delete()
	return redirect('emp_profile', pk = employee.id)

@login_required(login_url = 'login')
def settings(request):
	user = User.objects.get(username = request.user)
	edit_password = PasswordChange(user)
	edit_email = EmailChange(request.POST or None, instance = user)
	if edit_password.is_valid():
		edit_password.save()
		return redirect("settings")
	if edit_email.is_valid():
		edit_email.save()
		return redirect("settings")
	return render(request, 'settings.html', {"edit_password": edit_password, 'user': user, 'edit_email':edit_email})

def logout(request):
	auth.logout(request)
	return redirect('/')