
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from myapp.models import InformacaoDomicilio
from myapp.serializers import InformacaoDomicilioSerializer

class InformacaoDomicilioViewSet(viewsets.ModelViewSet):
    queryset = InformacaoDomicilio.objects.all()
    serializer_class = InformacaoDomicilioSerializer

    @action(detail=False, methods=['get'])
    def disponiveis(self, request):
        informacoes_domicilio = InformacaoDomiclio.objects.filter(disponivel=True)
        serializer = self.get_serializer(informacoes_domicilio, many=True)
        return Response(serializer.data)

