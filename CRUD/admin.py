from django.contrib import admin
from .models import Image
from import_export.admin import ImportExportModelAdmin

class ImageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'ImgName', 'ImgDetails')
    search_fields =['ImgName']
    ordering = ['id']

admin.site.register(Image, ImageAdmin)

# admin.site.register(Image)