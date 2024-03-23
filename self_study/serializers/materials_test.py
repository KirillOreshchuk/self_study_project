from rest_framework import serializers

from self_study.models import MaterialsTest


class MaterialsTestSerializer(serializers.ModelSerializer):
    """Сериализатор теста матариала"""

    class Meta:
        model = MaterialsTest
        fields = '__all__'
