from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Machine, Maintenance, Complaint, Dictionary
from .serializers import MachineSerializer, MaintenanceSerializer, ComplaintSerializer, DictionarySerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action
from django.http import JsonResponse
from urllib.parse import unquote
import logging



logger = logging.getLogger(__name__)

@api_view(['GET'])
def machine_detail_by_serial(request, serial_number):
    try:
        machine = Machine.objects.get(serial_number=serial_number)
        serializer = MachineSerializer(machine)
        return Response(serializer.data)
    except Machine.DoesNotExist:
        return Response({"detail": "Not found."}, status=404)

class DictionaryItemView(APIView):
    def get(self, request, name, format=None):
        try:
            name = unquote(name)
            logger.debug(f"Fetching dictionary item with name: {name}")
            dictionary_item = Dictionary.objects.get(name=name)
            serializer = DictionarySerializer(dictionary_item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Dictionary.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_engine_details(request, name):
    try:
        name = unquote(name)
        logger.debug(f"Fetching engine details with name: {name}")
        engine = Dictionary.objects.get(name=name)
        return JsonResponse({'name': engine.name, 'description': engine.description, 'model': engine.model})
    except Dictionary.DoesNotExist:
        return JsonResponse({'error': 'Engine not found'}, status=404)

@api_view(['GET'])
def get_transmission_details(request, name):
    try:
        name = unquote(name)
        logger.debug(f"Fetching transmission details with name: {name}")
        transmission = Dictionary.objects.get(name=name)
        return JsonResponse({'name': transmission.name, 'description': transmission.description, 'model': transmission.model})
    except Dictionary.DoesNotExist:
        return JsonResponse({'error': 'Transmission not found'}, status=404)

@api_view(['GET'])
def get_drive_axle_details(request, name):
    try:
        name = unquote(name)
        logger.debug(f"Fetching drive axle details with name: {name}")
        drive_axle = Dictionary.objects.get(name=name)
        return JsonResponse({'name': drive_axle.name, 'description': drive_axle.description, 'model': drive_axle.model})
    except Dictionary.DoesNotExist:
        return JsonResponse({'error': 'Drive axle not found'}, status=404)

@api_view(['GET'])
def get_steer_axle_details(request, name):
    try:
        name = unquote(name)
        logger.debug(f"Fetching steer axle details with name: {name}")
        steer_axle = Dictionary.objects.get(name=name)
        return JsonResponse({'name': steer_axle.name, 'description': steer_axle.description, 'model': steer_axle.model})
    except Dictionary.DoesNotExist:
        return JsonResponse({'error': 'Steer axle not found'}, status=404)

@api_view(['GET'])
def get_maintenance_type_details(request, name):
    try:
        maintenance_type = Dictionary.objects.get(name=name)
        return JsonResponse({'name': maintenance_type.name, 'description': maintenance_type.description, 'model': maintenance_type.model})
    except Dictionary.DoesNotExist:
        return JsonResponse({'error': 'Maintenance type not found'}, status=404)


@api_view(['GET'])
def get_organization_details(request, name):
    try:
        name = unquote(name)
        logger.debug(f"Fetching organization with name: {name}")
        organization = Dictionary.objects.get(name=name)
        return JsonResponse({'name': organization.name, 'description': organization.description})
    except Dictionary.DoesNotExist:
        return JsonResponse({'error': 'Organization not found'}, status=404)

@api_view(['GET'])
def get_service_company_details(request, name):
    try:
        name = unquote(name)
        logger.debug(f"Fetching service company with name: {name}")
        service_company = Dictionary.objects.get(name=name)
        return JsonResponse({'name': service_company.name, 'description': service_company.description})
    except Dictionary.DoesNotExist:
        return JsonResponse({'error': 'Service company not found'}, status=404)


@api_view(['GET'])
def get_failure_node_details(request, name):
    try:
        failure_node = Dictionary.objects.get(name=name)
        return JsonResponse({'name': failure_node.name, 'description': failure_node.description, 'model': failure_node.model})
    except Dictionary.DoesNotExist:
        return JsonResponse({'error': 'Failure node not found'}, status=404)


@api_view(['GET'])
def get_recovery_method_details(request, name):
    try:
        recovery_method = Dictionary.objects.get(name=name)
        return JsonResponse({'name': recovery_method.name, 'description': recovery_method.description, 'model': recovery_method.model})
    except Dictionary.DoesNotExist:
        return JsonResponse({'error': 'Recovery method not found'}, status=404)


class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        serial_number = self.request.query_params.get('serial_number', None)
        if serial_number:
            return Machine.objects.filter(serial_number=serial_number)
        return Machine.objects.all()

class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return Maintenance.objects.all()

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
        return Complaint.objects.all()

    @action(detail=False, methods=['get'])
    def all_complaints(self, request):
        complaints = self.get_queryset()
        serializer = self.get_serializer(complaints, many=True)
        return Response(serializer.data)
