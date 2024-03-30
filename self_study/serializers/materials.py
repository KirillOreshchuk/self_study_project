from rest_framework import serializers

from self_study.models import Materials


class MaterialsSerializer(serializers.ModelSerializer):
    """Сериализатор матариала"""

    class Meta:
        model = Materials
        fields = '__all__'
