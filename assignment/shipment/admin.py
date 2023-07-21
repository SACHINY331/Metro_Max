from django.contrib import admin

# Register your models here.
from .models import shipment,cargo,tracking

@admin.register(shipment)
class shipmentAdmin(admin.ModelAdmin):
    list_display=['origin','destination','expected_delivery_date','actual_delivery_date','status']

@admin.register(cargo)
class cargoAdmin(admin.ModelAdmin):
    list_display=['shipment','name','quantity']

@admin.register(tracking)
class trackingAdmin(admin.ModelAdmin):
    list_display=['shipment','status','location']    