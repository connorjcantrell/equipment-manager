from django.contrib import admin
from .models import Account, Location, WorkOrder, Labor


# Define the admin class
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass

@admin.register(WorkOrder)
class WorkOrderAdmin(admin.ModelAdmin):
    list_filter = ('status', 'call_type')

@admin.register(Labor)
class LaborAdmin(admin.ModelAdmin):
    pass
