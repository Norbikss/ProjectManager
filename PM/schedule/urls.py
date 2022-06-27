from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
path('', views.index, name = "index"),
path('login', views.login, name = "login"),
path('register', views.register, name = "register"),
path('logout', views.logout, name = "logout"),
path('settings', views.settings, name = "settings"),
path('add_employee', views.add_employee, name = "add_employee"),
path('show_employees', views.show_employees, name = "show_employees"),
path('create_schedule', views.create_schedule, name = "create_schedule"),
path('free_days', views.free_days, name = "free_days"),
path('edit_employee/<str:employee_id>', views.edit_employee, name = "edit_employee"),
path('profile/<str:pk>', views.emp_profile, name = "emp_profile"),
path('delete_employee/<str:employee_id>', views.delete_employee, name = "delete_employee"),
path('delete_vacation/<str:pk>', views.delete_vacation, name = "delete_vacation"),
path('delete_free_day/<str:pk>', views.delete_free_day, name = "delete_free_day"),
path('reset_password', auth_views.PasswordResetView.as_view(template_name="forget-pass.html"), name ="reset_password"),
path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="Succes-message.html"), name = "password_reset_done"),
path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset-form.html"), name = "password_reset_confirm"),
path('reset_done', auth_views.PasswordResetCompleteView.as_view(template_name="resset_completed.html"), name = "password_reset_complete"),
]