from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from .models import Profile, Employee, Vacation, Free_days

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
	employee = Employee.objects.get(id = pk)
	vacations = Vacation.objects.filter(employee = employee)
	free_days = Free_days.objects.filter(employee = employee)

	return render(request, 'profile.html', {'employee': employee, 'free_days': free_days, "vacations": vacations})

@login_required(login_url = 'login')
def logout(request):
	auth.logout(request)
	return redirect('/')