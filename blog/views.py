from django.shortcuts import render
from django.shortcuts import redirect
from .models import Blog, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def blog(request):
	all_blogs = Blog.objects.all()
	all_categories = Category.objects.all()

#Paginator

	paginator = Paginator(all_blogs, 4)	
	page = request.GET.get('page')		
	try:
		all_blogs = paginator.page(page)
	except PageNotAnInteger:
		all_blogs = paginator.page(1)
	except EmptyPage:
		all_blogs = paginator.page(paginator.num_pages)

	context = {
	'all_blogs': all_blogs,
	'all_categories': all_categories
	}
	return render (request, './blog/blog.html', context)

def single_blog(request, post_id):
  blog = Blog.objects.get(pk=post_id)
  return render(request, './blog/single_blog.html', {'blog': blog})
