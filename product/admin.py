from django.contrib import admin

# Register your models here.
from .models import Category,SubCategory,Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ("title",)
    prepopulated_fields={'slug': ('title',)}
    search_fields = ['title',]

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('title','category','ordering')
    list_filter = ("title",)
    prepopulated_fields={'slug': ('title',)}
    search_fields = ['title',]

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','subcategory','price')
    list_filter = ("title",)
    prepopulated_fields={'slug': ('title',)}
    search_fields = ['title', 'price']


admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(SubCategory,SubCategoryAdmin)

