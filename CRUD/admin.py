from django.contrib import admin
from .models import Image
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class ImageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    fields = ('id', 'ImgName', 'image', 'ImgDetails')
    list_display = ('id', 'ImgName', 'image', 'ImgDetails')    

admin.site.register(Image, ImageAdmin)

# admin.site.register(Image)