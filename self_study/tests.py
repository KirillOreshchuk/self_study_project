import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from self_study.models import Section, Materials, MaterialsTest
from users.models import User


class MaterialsTestCase(APITestCase):
    """Тестированиие эндпоинтов класса Materials"""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='user@test.com', password='password_test')
        self.client.force_authenticate(user=self.user)

        self.section = Section.objects.create(
            title='section test',
            description='section description test',
            user=self.user
        )

        self.material_test = MaterialsTest.objects.create(
            material_test='material_test test',
            material_test_answer='material_test_answer test',
            user=self.user
        )

        self.material = Materials.objects.create(
            title='title test',
            description='title description test',
            section=self.section,
            material_test=self.material_test,
            url='http://www.youtube.com/url_test',
            user=self.user
        )

    def test_list(self):
        """Тестирование вывода всех материалов"""

        response = self.client.get(reverse('self_study:materials_list'))

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results':
                    [
                        {
                            'id': self.material.pk,
                            'title': self.material.title,
                            'description': self.material.description,
                            'preview': None,
                            'date_create': datetime.datetime.strftime(self.material.date_create,
                                                                      "%Y-%m-%dT%H:%M:%S.%fZ"),
                            'url': self.material.url,
                            'section': self.section.pk,
                            'material_test': self.material_test.pk,
                            'user': self.user.pk
                        }
                    ]
            }

        )

    def test_retrieve(self):
        """Тестирование вывода одного материала"""

        response = self.client.get(reverse('self_study:materials_detail', kwargs={'pk': self.material.pk}))

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'id': self.material.pk,
                'title': self.material.title,
                'description': self.material.description,
                'preview': None,
                'date_create': datetime.datetime.strftime(self.material.date_create,
                                                          "%Y-%m-%dT%H:%M:%S.%fZ"),
                'url': self.material.url,
                'section': self.section.pk,
                'material_test': self.material_test.pk,
                'user': self.user.pk
            }
        )

    def test_create(self):
        """Тестирование создания материала"""

        data = {
            'title': 'title test create'
        }

        response = self.client.post(
            reverse('self_study:materials_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json()['title'],
            'title test create'
        )

        self.assertTrue(Materials.objects.all().exists())

    def test_update(self):
        """Тестирование изменения материала"""

        response = self.client.put(
            reverse('self_study:materials_update', kwargs={'pk': self.material.pk}),
            data={'title': 'title test update'}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['title'],
            'title test update'
        )

    def test_delete(self):
        """Тестирование удаления материала"""

        response = self.client.delete(reverse('self_study:materials_delete', kwargs={'pk': self.material.pk}))

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
