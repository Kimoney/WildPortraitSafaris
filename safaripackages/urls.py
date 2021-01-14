from django.urls import path
from django.conf.urls import url
from .views import safaripackages_view, single_safaripackage, safaripackage_categories

app_name = 'safaripackages'

urlpatterns = [
	path('safaripackages/', safaripackages_view, name='safaripackages_view'),
	path('safaripackages/<post_id>/', single_safaripackage, name='single_safaripackage'),
	path('categories/<slug:slug>', safaripackage_categories, name='safaricategory'),
]