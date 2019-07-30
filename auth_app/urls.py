from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import CustomPasswordResetForm
urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html', form_class=CustomPasswordResetForm), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('check_availability/', views.check_availability, name='check_availability')
]
