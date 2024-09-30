from django.shortcuts import render, redirect
from .forms import PaymentForm, InvoiceForm
from .models import Transaction, Invoice
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
import requests


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=email, password=password)
        if user is not None:
            # Log in the user and redirect to the desired page
            login(request, user)
            return redirect('home')  # Redirect to home or the next page
        else:
            # Invalid login attempt
            messages.error(request, 'Invalid email or password.')

    return render(request, 'login.html')


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


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # This will save the user in the database
            messages.success(request, 'Registration successful. Welcome to TAPPESA!')
            return redirect('login')  # Redirect to the login page after successful registration
        else:
            messages.error(request, 'There was an error in your registration. Please try again.')
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})
def dashboard(request):
    return render(request, 'dashboard.html')



def make_payment(request):
    return render(request, 'make_payment.html')

# def register_view(request):
#     return render(request, 'register.html')

def request_password_reset(request):
    return render(request, 'password_reset.html')

def resend_verification_email(request):
    return render(request, 'resend_verification_email.html')


@login_required  # Ensure that only logged-in users can access the home page
def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')  # Ensure 'contact.html' exists in your templates directory
