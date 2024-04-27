from django.contrib import admin

# Register your models here.
from .models import Client, Product, ClientProduct, Transaction, Type_transaction

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(ClientProduct)
admin.site.register(Transaction)
admin.site.register(Type_transaction)
# Compare this snippet from finance/views.py:
# from django.shortcuts import render
