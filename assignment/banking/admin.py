from django.contrib import admin

# Register your models here.
from .models import account,customer

@admin.register(account)
class accountAdmin(admin.ModelAdmin):
    list_display=['account_number','balance','account_type']

@admin.register(customer)
class customerAdmin(admin.ModelAdmin):
    list_display=['name','email','phone_number','addres',]