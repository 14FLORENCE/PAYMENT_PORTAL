from django.contrib import admin

# Register your models here.
from .models import Transaction, Invoice

admin.site.register(Transaction)
admin.site.register(Invoice)
