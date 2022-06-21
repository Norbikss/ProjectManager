from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
path('index', views.index, name = "index"),
path('', views.login, name = "login"),
path('register', views.register, name = "register"),
path('logout', views.logout, name = "logout"),
path('reset_password', auth_views.PasswordResetView.as_view(template_name="forget-pass.html"), name ="reset_password"),
path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="Succes-message.html"), name = "password_reset_done"),
path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset-form.html"), name = "password_reset_confirm"),
path('reset_done', auth_views.PasswordResetCompleteView.as_view(template_name="resset_completed.html"), name = "password_reset_complete"),
]