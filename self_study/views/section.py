from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from self_study.models import Section
from self_study.paginators import SelfStudyPaginator
from self_study.serializers.section import SectionSerializer
from users.permissions import IsOwner


class SectionViewSet(ModelViewSet):
    """ViewSet раздела"""
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    pagination_class = SelfStudyPaginator

    def perform_create(self, serializer):
        """Функция привязывает пользователя к созданному им разделу"""
        new_section = serializer.save()
        new_section.user = self.request.user
        new_section.save()

    def get_permissions(self):
        """Функция переопределяет права доступа"""
        if self.action == 'create' or self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update' or self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in permission_classes]
