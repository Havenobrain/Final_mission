from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Machine, Maintenance, Complaint, Dictionary
from .serializers import MachineSerializer, MaintenanceSerializer, ComplaintSerializer, DictionarySerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action

@api_view(['GET'])
def machine_detail_by_serial(request, serial_number):
    try:
        machine = Machine.objects.get(serial_number=serial_number)
        serializer = MachineSerializer(machine)
        return Response(serializer.data)
    except Machine.DoesNotExist:
        return Response({"detail": "Not found."}, status=404)


class DictionaryItemView(APIView):
    def get(self, request, id, format=None):
        try:
            dictionary_item = Dictionary.objects.get(id=id)
            serializer = DictionarySerializer(dictionary_item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Dictionary.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)



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
            permission_classes = [IsAuthenticated]
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

@api_view(['GET'])
def machine_detail_by_serial(request, serial_number):
    try:
        machine = Machine.objects.get(serial_number=serial_number)
        serializer = MachineSerializer(machine)
        return Response(serializer.data)
    except Machine.DoesNotExist:
        return Response({"detail": "Not found."}, status=404)
