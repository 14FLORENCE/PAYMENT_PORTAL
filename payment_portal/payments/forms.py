from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from phonenumber_field.formfields import PhoneNumberField
from .models import Invoice

class PaymentForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    payment_method = forms.ChoiceField(choices=[('paypal', 'PayPal'), ('mpesa', 'M-PESA')])

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['amount']


class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)
    phone_number = PhoneNumberField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    password_repeat = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['full_name', 'email', 'phone_number', 'password', 'password_repeat']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')

        if password and password_repeat and password != password_repeat:
            raise ValidationError("Passwords do not match.")

        return cleaned_data
