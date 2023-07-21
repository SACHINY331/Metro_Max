from django.contrib import admin

# Register your models here.
from .models import product,category

@admin.register(product)
class prductAdmin(admin.ModelAdmin):
    list_display=['name','description','price','created_at']

@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display=['name']


    # @admin.display(description='categories')
    # def get_categories(self):
    #     return [category.name for category in self.categories.all]