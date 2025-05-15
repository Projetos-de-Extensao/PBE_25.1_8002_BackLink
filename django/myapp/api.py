from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from myapp.models import Domicilio, Morador
from myapp.serializers import DomicilioSerializer, MoradorSerializer

class MoradorViewSet(viewsets.ModelViewSet):
    queryset = Morador.objects.all()
    serializer_class = MoradorSerializer

class DomicilioViewSet(viewsets.ModelViewSet):
    queryset = Domicilio.objects.all()
    serializer_class = DomicilioSerializer

    @action(detail=False, methods=['get'])
    def disponiveis(self, request):
        domicilios = Domicilio.objects.filter(disponivel=True)
        serializer = self.get_serializer(domicilios, many=True)
        return Response(serializer.data)

