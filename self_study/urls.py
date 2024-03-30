from django.urls import path
from rest_framework import routers

from self_study.apps import SelfStudyConfig
from self_study.views.materials_test import MaterialsTestViewSet, MaterialsTestCheckAPIView
from self_study.views.section import SectionViewSet
from self_study.views.materials import (MaterialsListView, MaterialsCreateView, MaterialsDetailView,
                                        MaterialsUpdateView, MaterialsDeleteView)

app_name = SelfStudyConfig.name


urlpatterns = [
    path('materials/', MaterialsListView.as_view(), name='materials_list'),
    path('materials/create/', MaterialsCreateView.as_view(), name='materials_create'),
    path('materials/<int:pk>/', MaterialsDetailView.as_view(), name='materials_detail'),
    path('materials/update/<int:pk>/', MaterialsUpdateView.as_view(), name='materials_update'),
    path('materials/delete/<int:pk>/', MaterialsDeleteView.as_view(), name='materials_delete'),


    path('materials_test_answer_check/', MaterialsTestCheckAPIView.as_view(), name='materials_test_answer_check'),
]

router = routers.SimpleRouter()
router.register('section', SectionViewSet)
router.register('materials_test', MaterialsTestViewSet)

urlpatterns += router.urls
