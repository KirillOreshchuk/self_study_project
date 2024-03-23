from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from self_study.models import MaterialsTest
from self_study.paginators import SelfStudyPaginator
from self_study.serializers.materials_test import MaterialsTestSerializer
from users.permissions import IsOwner


class MaterialsTestViewSet(ModelViewSet):
    """ViewSet теста материала"""
    queryset = MaterialsTest.objects.all()
    serializer_class = MaterialsTestSerializer
    pagination_class = SelfStudyPaginator

    def perform_create(self, serializer):
        """Функция привязывает пользователя к созданному им тесту материала"""
        new_material_test = serializer.save()
        new_material_test.user = self.request.user
        new_material_test.save()

    def get_permissions(self):
        """Функция переопределяет права доступа"""
        if self.action == 'create' or self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update' or self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in permission_classes]
