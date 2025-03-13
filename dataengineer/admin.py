# from django.contrib import admin
# from .models import ImageModel

# @admin.register(ImageModel)
# class ImageModelAdmin(admin.ModelAdmin):
#     list_display = ['name', 'image','file_size','created_at'] 

from django.contrib import admin
from django.utils.html import format_html
from .models import ImageModel, ProjectModel

class ImageModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'thumbnail', 'file_size', 'created_at')
    readonly_fields = ('thumbnail',)

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 5px;"/>', obj.image.url)
        return "No Image"

    thumbnail.short_description = "Thumbnail"

admin.site.register(ProjectModel)
admin.site.register(ImageModel, ImageModelAdmin)
