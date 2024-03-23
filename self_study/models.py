from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Section(models.Model):
    """Модель раздела"""

    title = models.CharField(max_length=100, verbose_name='Раздел')
    description = models.TextField(**NULLABLE, verbose_name='Описание раздела')
    preview = models.ImageField(upload_to='self_study/', **NULLABLE, verbose_name='Превью-раздел')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания раздела')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                             verbose_name='Пользователь')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class Materials(models.Model):
    """Модель материала"""

    title = models.CharField(max_length=100, verbose_name='Материал')
    description = models.TextField(**NULLABLE, verbose_name='Описание материала')
    section = models.ForeignKey('self_study.Section', on_delete=models.SET_NULL, null=True,
                                verbose_name='Раздел', related_name='material')
    preview = models.ImageField(upload_to='self_study/', **NULLABLE, verbose_name='Превью-материал')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания материала')
    url = models.URLField(**NULLABLE, verbose_name='Ссылка на материал')
    material_test = models.ForeignKey('MaterialsTest', on_delete=models.CASCADE, **NULLABLE,
                                      verbose_name='Тест материала')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                             verbose_name='Пользователь')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class MaterialsTest(models.Model):
    """Модель тестов материала"""

    material_test = models.CharField(max_length=300, **NULLABLE, verbose_name='Тест материала')
    material_test_answer = models.CharField(max_length=100, **NULLABLE, verbose_name='Ответ на тест материала')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                             verbose_name='Пользователь')

    def __str__(self):
        return f'Тест: {self.material_test}, Ответ: {self.material_test_answer}'

    class Meta:
        verbose_name = 'Тест материала'
        verbose_name_plural = 'Тесты материалов'
