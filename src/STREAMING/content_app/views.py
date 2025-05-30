from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Content
from .serializers import ContentSerializer


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(creator=self.request.user)


class ContentListView(generics.ListAPIView):
    serializer_class = ContentSerializer

    def get_queryset(self):
        queryset = Content.objects.all()
        content_type = self.request.query_params.get('content_type')

        if content_type in [choice[0] for choice in Content.CONTENT_TYPE_CHOICES]:
            queryset = queryset.filter(content_type=content_type)

        return queryset
