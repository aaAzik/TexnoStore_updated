from django.contrib import admin
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =  ['id','name','description','price']
    list_filter = ['name']
    search_fields = ['name']
    prepopulated_fields = {"slug": ["name"]}

admin.site.register(Category)
