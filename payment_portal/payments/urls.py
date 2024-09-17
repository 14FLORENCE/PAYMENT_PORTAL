from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# app_name = 'payments'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
     # Login URL (using Django's built-in login view)
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # Register URL (if you have a custom registration view)
    path('register/', views.register, name='register'),

    # Password reset URLs (Django provides built-in views)
    path('register/request_password_reset/', auth_views.PasswordResetView.as_view(), name='request_password_reset'),    path('/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Resend verification email (if you have a custom view)
    path('register/resend_verification_email/', views.resend_verification_email, name='resend_verification_email'),

    path('about/', views.about, name='about'),  # About Us page
    path('contact/', views.contact, name='contact'),  # Contact Us page
    path('make/', views.make_payment, name='make_payment'),
    path('invoice/', views.generate_invoice, name='generate_invoice'),
]
