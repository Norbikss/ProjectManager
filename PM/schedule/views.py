from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm

# Create your views here.
@login_required(login_url = '/')
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
				#log user and redirect to settings page
				user_login = auth.authenticate(username=username, password=password)
				auth.login(request, user_login)
				return redirect('index')
		else:
			messages.info(request, 'Password Not Matching')
			return redirect('register')
	return render(request, 'register.html')


@login_required(login_url='/')
def logout(request):
	auth.logout(request)
	return redirect('/')