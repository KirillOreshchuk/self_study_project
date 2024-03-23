from rest_framework import serializers

from self_study.models import Section


class SectionSerializer(serializers.ModelSerializer):
    """Сериализатор раздела"""

    class Meta:
        model = Section
        fields = '__all__'
