from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from self_study.models import MaterialsTest
from self_study.paginators import SelfStudyPaginator
from self_study.serializers.materials_test import MaterialsTestSerializer
from users.permissions import IsOwner, IsStaffOrSuperuser


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
            permission_classes = [IsAuthenticated, IsOwner | IsStaffOrSuperuser]
        return [permission() for permission in permission_classes]


class MaterialsTestCheckAPIView(APIView):
    """ Отвечает за ввод ответа на тест и показ правильного ответа """
    queryset = MaterialsTest.objects.all()
    serializer_class = MaterialsTestSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = MaterialsTestSerializer(data=request.data)

        if serializer.is_valid():
            data = request.data
            materials_test_answer = data['materials_test_answer'].lower()
            id_test = data['id_test']
            test = MaterialsTest.objects.get(id=id_test)
            if materials_test_answer != test.material_test_answer.lower():
                return Response(f'Неверно, правильный ответ - {test.material_test_answer}')
            else:
                return Response('Верный ответ!')
        else:
            data = serializer.errors
            return Response(data)
