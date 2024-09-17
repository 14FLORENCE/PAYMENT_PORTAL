from django.shortcuts import render, redirect
from .forms import PaymentForm, InvoiceForm
from .models import Transaction, Invoice
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
import requests

@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user)
    invoices = Invoice.objects.filter(user=request.user)
    return render(request, 'payments/dashboard.html', {'transactions': transactions, 'invoices': invoices})

@login_required
def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            payment_method = form.cleaned_data['payment_method']
            # Integrate with payment API here
            # Example for PayPal:
            if payment_method == 'paypal':
                # Make API call to PayPal
                pass
            # Log the transaction
            Transaction.objects.create(user=request.user, amount=amount, transaction_type='Payment')
            return redirect('dashboard')
    else:
        form = PaymentForm()
    return render(request, 'payments/make_payment.html', {'form': form})

@login_required
def generate_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.user = request.user
            invoice.save()
            # Generate PDF and QR code
            # Example code to generate PDF and QR code
            return redirect('dashboard')
    else:
        form = InvoiceForm()
    return render(request, 'payments/generate_invoice.html', {'form': form})

# def register(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your account has been created successfully.')
#             return redirect('dashboard')  # Redirect to login page after successful registration
#         else:
#             messages.error(request, 'Please correct the errors below.')
#     else:
#         form = SignUpForm()
#     return render(request, 'register.html', {'form': form})

def register(request):
    return render(request, 'register.html')  # Ensure this view exists


def dashboard(request):
    return render(request, 'dashboard.html')

# def login(request):
#     # Handle login logic here
#     return render(request, 'login.html')  # Adjust the template name as needed


def login_view(request):
    return render(request, 'login.html')

# def register_view(request):
#     return render(request, 'register.html')

def request_password_reset(request):
    return render(request, 'password_reset.html')

def resend_verification_email(request):
    return render(request, 'resend_verification_email.html')
def about(request):
    return render(request, 'about.html')  # Ensure 'about.html' exists in your templates directory

def contact(request):
    return render(request, 'contact.html')  # Ensure 'contact.html' exists in your templates directory
