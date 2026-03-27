from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from ad.models import Ad
from ad.serializers import AdSerializer
from users.permissions import Moderator, IsOwner


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'description']

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.subscription:
            return Ad.objects.order_by('-is_premium', '-date_created')
        return Ad.objects.all().order_by('-date_created')

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        elif self.action in ['update', 'partial_update']:
            self.permission_classes = [IsOwner]
        elif self.action == 'delete':
            self.permission_classes = [IsOwner | Moderator]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        """Привязываем текущего пользователя к создаваемому объекту"""
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()
