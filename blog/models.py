from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here

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

    def __str__(self):
        return self.title


class Blog(models.Model):
	title = models.CharField(max_length=200)
	introduction = models.CharField(max_length=280, default=1)
	body = models.TextField()
	image = models.ImageField(upload_to='blog/%Y/%m/%d', null=True)
	image2 = models.ImageField(upload_to='blog/%Y/%m/%d', null=True)
	slug = models.SlugField(max_length=200, unique=True)
	author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
	publish = models.BooleanField(default=True)
	created = models.DateTimeField(default=timezone.now, editable=False)
	modified = models.DateTimeField(auto_now=True)
	category = models.ManyToManyField(Category)

	objects = EntryQuerySet.as_manager()

	def __str__(self):
		return self.title
		
	class Meta:
		verbose_name = 'Blog Entry'
		verbose_name_plural = 'Blog Entries'
		ordering = ["-created", "-modified"]