"""WildPortraitSafaris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages.views import home_view, about_us_view, contact_us_view, faq_view, inquiry_view, the_team_view
from blog.views import blog, single_blog
from safaripackages.views import safaripackages_view, single_safaripackage, safaripackage_categories
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('about/', about_us_view, name='about_us'),
    path('team',the_team_view, name='the_team'),
    path('inquiry/', inquiry_view, name='inquiry'),
    path('contact/', contact_us_view, name='contact_us'),
    path('faq', faq_view, name='faq'),
    path('',include('safaripackages.urls')),
    #path('safaripackages/<category_slug>/', include('safaripackages.urls'), safaripackage_categories, name='safaricategory'),
   # path('single_safaripackage/<post_id>/', single_safaripackage, name='single_safaripackage'),
    path('blog/', blog, name='blog'),
    path('blog/<slug:slug>/', single_blog, name='single_blog')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
