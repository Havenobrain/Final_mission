from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Machine, Maintenance, Complaint
from .serializers import MachineSerializer, MaintenanceSerializer, ComplaintSerializer
from .permissions import IsManager, IsServiceCompany, IsClient

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Machine.objects.all().only('serial_number', 'model', 'engine_model', 'transmission_model', 'drive_axle_model', 'steer_axle_model')
        elif user.groups.filter(name='Клиент').exists():
            return Machine.objects.filter(client=user)
        elif user.groups.filter(name='Сервисная организация').exists():
            return Machine.objects.filter(service_company=user)
        elif user.groups.filter(name='Менеджер').exists():
            return Machine.objects.all()
        else:
            return Machine.objects.none()

class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsManager | IsServiceCompany]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Менеджер').exists():
            return Maintenance.objects.all()
        elif user.groups.filter(name='Сервисная организация').exists():
            return Maintenance.objects.filter(machine__service_company=user)
        elif user.groups.filter(name='Клиент').exists():
            return Maintenance.objects.filter(machine__client=user)
        else:
            return Maintenance.objects.none()

class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsManager | IsServiceCompany]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Менеджер').exists():
            return Complaint.objects.all()
        elif user.groups.filter(name='Сервисная организация').exists():
            return Complaint.objects.filter(machine__service_company=user)
        elif user.groups.filter(name='Клиент').exists():
            return Complaint.objects.filter(machine__client=user)
        else:
            return Complaint.objects.none()

    @action(detail=False, methods=['get'])
    def all_complaints(self, request):
        complaints = self.get_queryset()
        serializer = self.get_serializer(complaints, many=True)
        return Response(serializer.data)
