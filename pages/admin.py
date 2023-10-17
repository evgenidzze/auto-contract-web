from django.contrib import admin

from pages.models import So, Department, Object, ConsumerCategory


class SoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'director', 'document_num', 'date']


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department', 'id', 'code', 'address']


class ObjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'so', 'department']

class ConsumerCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(So, SoAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Object, ObjectAdmin)
admin.site.register(ConsumerCategory, ConsumerCategoryAdmin)
