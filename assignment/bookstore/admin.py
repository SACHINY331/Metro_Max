from django.contrib import admin

# Register your models here.
from .models import book,author,review

@admin.register(book)
class bookAdmin(admin.ModelAdmin):
    list_display=['title','author','price','publication_date','discription','image']

@admin.register(author)
class commentAdmin(admin.ModelAdmin):
    list_display=['name','biography','photo']

@admin.register(review)
class commentAdmin(admin.ModelAdmin):
    list_display=['book','content','rating']    