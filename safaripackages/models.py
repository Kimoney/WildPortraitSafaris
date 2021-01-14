from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class EntryQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish=True)


class Category(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


#    def get_absolute_url(self):
#    	return reverse('safaripackages:safaripackage_categories', args=[self.slug])


    def __str__(self):
        return self.title


class SafariPackages(models.Model):
	image = models.ImageField(upload_to='SafariPackages/%Y/%m/%d', null=False)
	title = models.CharField(max_length=200)
	cost = models.FloatField(null=False)
	days = models.FloatField(blank=False, null=False)
	nights = models.FloatField(blank=False, null=False)
	category = models.ManyToManyField(Category, related_name='posts')
	exodus = models.CharField(max_length=200)
	destination = models.CharField(max_length=200)
	overview = models.TextField(max_length=140, null=False)
	brief_description = models.TextField(max_length=400, null=False, blank=False)
	slug = models.SlugField(max_length=200, unique=True)


	objects = EntryQuerySet.as_manager()

	def __str__(self):
		return self.title
		
	class Meta:
		verbose_name = 'Safari Package Entry'
		verbose_name_plural = 'Safari Package Entries'

class DayNumber(models.Model):
	daydetails = models.ForeignKey(SafariPackages, related_name='daydetails', default=1, on_delete=models.SET_DEFAULT)
	day_number = models.CharField( max_length=10, null=True, blank=True)
	location = models.CharField(max_length=200, null=True, blank=True)
	image = models.ImageField (upload_to='SafariPackagesDetails/%Y/%m/%d', null=False, default=1)
	day_description = models.TextField()