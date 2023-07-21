from django.contrib import admin

# Register your models here.
from .models import blog,comment

@admin.register(blog)
class blogAdmin(admin.ModelAdmin):
    list_display=['title','author','publication_date','content']

@admin.register(comment)
class commentAdmin(admin.ModelAdmin):
    list_display=['post','content','created_at']