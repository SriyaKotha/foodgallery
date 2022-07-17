from django.contrib import admin
from .models import Image
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin

class ImageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    fields = ('id', 'ImgName', 'ImgDetails')
    list_display = ('id', 'ImgName', 'ImgDetails')
    search_fields =['ImgName']
    ordering = ['id']

admin.site.register(Image, ImageAdmin)

# admin.site.register(Image)