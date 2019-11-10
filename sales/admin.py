

from django.contrib import admin
from .models import Customer, Order


class CustomerList(admin.ModelAdmin):
    list_display = ('customer_id', 'company', 'phone_number')
    list_filter = ('customer_id', 'company', 'phone_number')
    search_fields = ('customer_id', 'company', 'phone_number')
    ordering = ['customer_id']


class OrderList (admin.ModelAdmin):
    list_display = ('customer','order_number', 'status',)
    list_filter = ('customer','order_number', 'status')
    search_fields = ('customer','order_number', 'status')
    ordering = ['order_number']

# Register your models here.


admin.site.register(Customer)
admin.site.register(Order)
