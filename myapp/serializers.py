from rest_framework import serializers
from .models import Machine, Maintenance, Complaint

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'
        read_only_fields = ['client', 'service_company']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user = self.context['request'].user

        if not user.is_authenticated:
            allowed_fields = ['serial_number', 'model', 'engine_model', 'transmission_model', 'drive_axle_model', 'steer_axle_model']
            representation = {field: representation[field] for field in allowed_fields}

        return representation

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = '__all__'

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'

