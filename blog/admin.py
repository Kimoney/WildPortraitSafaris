from django.contrib import admin
from .models import Blog, Category

class CategoryAdmin(admin.ModelAdmin):
	list_display = ("title",)
	prepopulated_fields = {"slug":("title",)}

admin.site.register(Category, CategoryAdmin)

class BlogAdmin(admin.ModelAdmin):
	list_display = ("title", "created", "modified")
	prepopulated_fields = {"slug": ("title",)}

# Register your models here.

admin.site.register(Blog, BlogAdmin)