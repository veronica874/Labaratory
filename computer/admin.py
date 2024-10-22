from django.contrib import admin
from .models import Labaratory, Lab_attendant, Computer  # Import the actual models

# Register your models here.
class LabaratoryAdmin(admin.ModelAdmin):
    list_display = ("lab_name", "location", "number_of_computers")  # Updated field names


class LabAttendantAdmin(admin.ModelAdmin):
    list_display = ("attendant_name", "gender", "age", "address", "labaratory")


class ComputersAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "ram", "lab")


# Register the models with their respective admin classes
admin.site.register(Labaratory, LabaratoryAdmin)
admin.site.register(Lab_attendant, LabAttendantAdmin)
admin.site.register(Computer, ComputersAdmin)
