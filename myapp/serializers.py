from rest_framework import serializers
from .models import Machine, Maintenance, Complaint, Dictionary

class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = ['name', 'description', 'model'] 

class MachineSerializer(serializers.ModelSerializer):
    model = serializers.CharField(source='model.name', required=False)
    engine_model = serializers.CharField(source='engine_model.name', required=False)
    transmission_model = serializers.CharField(source='transmission_model.name', required=False)
    drive_axle_model = serializers.CharField(source='drive_axle_model.name', required=False)
    steer_axle_model = serializers.CharField(source='steer_axle_model.name', required=False)

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
    maintenance_type = DictionarySerializer(read_only=True)
    service_company = serializers.CharField(source='service_company.username', required=False)
    machine = MachineSerializer(read_only=True)
    organization = DictionarySerializer(read_only=True)

    class Meta:
        model = Maintenance
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user = self.context['request'].user

        if not user.is_authenticated:
            allowed_fields = ['machine', 'maintenance_type', 'maintenance_date', 'runtime_hours', 'order_number', 'order_date', 'organization', 'service_company']
            representation = {field: representation[field] for field in allowed_fields}

        return representation

class ComplaintSerializer(serializers.ModelSerializer):
    machine = MachineSerializer(read_only=True)
    failure_node = DictionarySerializer(read_only=True)
    recovery_method = DictionarySerializer(read_only=True)
    service_company = serializers.CharField(source='service_company.username', required=False)

    class Meta:
        model = Complaint
        fields = '__all__'

