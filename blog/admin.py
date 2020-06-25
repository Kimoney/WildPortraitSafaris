from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
	list_display = ("title", "created", "modified")
	prepopulated_fields = {"slug": ("title",)}

# Register your models here.

admin.site.register(Blog, BlogAdmin)