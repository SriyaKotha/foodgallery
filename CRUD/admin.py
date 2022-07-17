from django.contrib import admin
from .models import Image
from django.utils.safestring import mark_safe

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    fields = ('id', 'ImgName', 'image', 'ImgDetails')
    list_display = ('id', 'ImgName', 'image', 'ImgDetails')
    search_fields =['ImgName']
    ordering = ['id']
    readonly_fields = ['image']

    def image(self, obj):
        return mark_safe('<img src="{url}" width="100" height="100"/>'.format(
            url = obj.ImgURL,
            )
    )


admin.site.register(Image, ImageAdmin)

# admin.site.register(Image)