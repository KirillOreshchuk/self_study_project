from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from self_study.models import Materials
from self_study.paginators import SelfStudyPaginator
from users.permissions import IsOwner
from self_study.serializers.materials import MaterialsSerializer


class MaterialsListView(ListAPIView):
    """Отображение списка материалов"""
    queryset = Materials.objects.all()
    serializer_class = MaterialsSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = SelfStudyPaginator


class MaterialsCreateView(CreateAPIView):
    """Создание матириала"""
    queryset = Materials.objects.all()
    serializer_class = MaterialsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Функция привязывает пользователя к созданному им материалу"""
        new_material = serializer.save()
        new_material.user = self.request.user
        new_material.save()


class MaterialsDetailView(RetrieveAPIView):
    """Отображение одного материала"""
    queryset = Materials.objects.all()
    serializer_class = MaterialsSerializer
    permission_classes = [IsAuthenticated]


class MaterialsUpdateView(UpdateAPIView):
    """Изменение материала"""
    queryset = Materials.objects.all()
    serializer_class = MaterialsSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class MaterialsDeleteView(DestroyAPIView):
    """Удаление материала"""
    queryset = Materials.objects.all()
    serializer_class = MaterialsSerializer
    permission_classes = [IsAuthenticated, IsOwner]
