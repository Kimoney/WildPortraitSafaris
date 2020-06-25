from django.contrib import admin
from .models import SafariPackages, Category, DayNumber

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	list_display = ("title",)
	prepopulated_fields = {"slug":("title",)}

admin.site.register(Category, CategoryAdmin)
		

class DayNumberInline(admin.StackedInline):
	model = DayNumber


class SafariPackagesAdmin(admin.ModelAdmin):
	list_display = ("title", "destination", "cost")
	prepopulated_fields = {"slug": ("title",)}
	inlines = [
		DayNumberInline,
	]

admin.site.register(SafariPackages, SafariPackagesAdmin)