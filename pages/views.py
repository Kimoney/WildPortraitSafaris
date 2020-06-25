from django.shortcuts import render
from django.http import HttpResponse
import safaripackages
import blog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home_view(request):

	all_safaripackages = safaripackages.models.SafariPackages.objects.all()

#Paginator

	paginator = Paginator(all_safaripackages, 4)	
	page = request.GET.get('page')		
	try:
		all_safaripackages = paginator.page(page)
	except PageNotAnInteger:
		all_safaripackages = paginator.page(1)
	except EmptyPage:
		all_safaripackages = paginator.page(paginator.num_pages)


	all_blogs = blog.models.Blog.objects.all()

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
	'all_safaripackages': all_safaripackages,
	'all_blogs': all_blogs
	}


	return render (request, "./main/index.html", context)

def about_us_view(request):
	return render (request, "./main/about_us.html")

def inquiry_view(request):
	return render (request, "./main/inquiryform.html")

def contact_us_view(request):
	return render (request, "./main/contact_us.html")

def faq_view(request):
	return render (request, "./main/faq.html")