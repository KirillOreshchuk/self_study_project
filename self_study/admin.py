from django.contrib import admin

from self_study.models import Section, Materials, MaterialsTest


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'preview', 'user')


@admin.register(Materials)
class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'preview', 'url', 'section', 'user')
    ordering = ('id',)


@admin.register(MaterialsTest)
class MaterialsTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'material_test', 'material_test_answer',)
