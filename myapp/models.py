from django.db import models
from django.contrib.auth.models import User


class Dictionary(models.Model):
    name = models.CharField(max_length=100)  
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Machine(models.Model):
    serial_number = models.CharField(max_length=255, unique=True)
    model = models.ForeignKey(Dictionary, on_delete=models.CASCADE, related_name='machines_as_model')
    engine_model = models.ForeignKey(Dictionary, on_delete=models.CASCADE, related_name='machines_as_engine_model')
    engine_number = models.CharField(max_length=255)
    transmission_model = models.ForeignKey(Dictionary, on_delete=models.CASCADE, related_name='machines_as_transmission_model')
    transmission_number = models.CharField(max_length=255)
    drive_axle_model = models.ForeignKey(Dictionary, on_delete=models.CASCADE, related_name='machines_as_drive_axle_model')
    drive_axle_number = models.CharField(max_length=255)
    steer_axle_model = models.ForeignKey(Dictionary, on_delete=models.CASCADE, related_name='machines_as_steer_axle_model')
    steer_axle_number = models.CharField(max_length=255)
    supply_date = models.DateField()
    client = models.CharField(max_length=255)
    end_user = models.CharField(max_length=255)
    delivery_address = models.TextField()
    additional_options = models.TextField()
    service_company = models.CharField(max_length=255)

    def __str__(self):
        return self.serial_number

class Maintenance(models.Model):
    maintenance_type = models.ForeignKey(Dictionary, on_delete=models.CASCADE, related_name='maintenances_as_type')
    maintenance_date = models.DateField()
    runtime_hours = models.IntegerField()
    order_number = models.CharField(max_length=100)
    order_date = models.DateField()
    organization = models.ForeignKey(Dictionary, on_delete=models.CASCADE, related_name='maintenances_as_organization')
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='maintenances_as_machine')
    service_company = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='maintenances_as_service_company')
    maintenance_organization = models.CharField(max_length=255)
    operating_hours = models.IntegerField()
    downtime = models.IntegerField()
    recovery_method = models.TextField()

    def __str__(self):
        return f"{self.machine.serial_number} - {self.maintenance_type.name} - {self.maintenance_date}"



class Complaint(models.Model):
    machine = models.ForeignKey('Machine', on_delete=models.CASCADE, related_name='complaints')
    complaint_date = models.DateField()
    operating_hours = models.IntegerField()
    failure_node = models.ForeignKey('Dictionary', on_delete=models.CASCADE, related_name='complaints_as_failure_node')
    failure_description = models.TextField()
    recovery_method = models.ForeignKey('Dictionary', on_delete=models.CASCADE, related_name='complaints_as_recovery_method')
    parts_used = models.TextField()
    recovery_date = models.DateField()
    downtime = models.IntegerField()
    service_company = models.ForeignKey(User, on_delete=models.CASCADE, related_name='complaints_as_service_company')

    def save(self, *args, **kwargs):
        if self.complaint_date and self.recovery_date:
            self.downtime = (self.recovery_date - self.complaint_date).days
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.machine.serial_number} - {self.complaint_date}"


from django.db import models
from django.contrib.auth.models import Group, Permission

def create_groups_and_permissions():
    client_group, created = Group.objects.get_or_create(name='Клиент')
    service_group, created = Group.objects.get_or_create(name='Сервисная организация')
    manager_group, created = Group.objects.get_or_create(name='Менеджер')

    view_machine = Permission.objects.get(codename='view_machine')
    add_maintenance = Permission.objects.get(codename='add_maintenance')
    view_maintenance = Permission.objects.get(codename='view_maintenance')
    add_complaint = Permission.objects.get(codename='add_complaint')
    view_complaint = Permission.objects.get(codename='view_complaint')

    client_group.permissions.add(view_machine, view_maintenance, add_maintenance, view_complaint)
    service_group.permissions.add(view_machine, view_maintenance, add_maintenance, view_complaint, add_complaint)
    manager_group.permissions.add(view_machine, add_maintenance, view_maintenance, add_complaint, view_complaint)
