from django.contrib import admin
from .models import Machine, Maintenance, Complaint, Dictionary

admin.site.register(Machine)
admin.site.register(Maintenance)
admin.site.register(Complaint)
admin.site.register(Dictionary)
