from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import SafariPackages, DayNumber, Category

# Create your views here.
def safaripackages_view(request):
	all_safaripackages = SafariPackages.objects.all()
	all_categories = Category.objects.all()

#Paginator

	paginator = Paginator(all_safaripackages, 12)	
	page = request.GET.get('page')		
	try:
		all_safaripackages = paginator.page(page)
	except PageNotAnInteger:
		all_safaripackages = paginator.page(1)
	except EmptyPage:
		all_safaripackages = paginator.page(paginator.num_pages)


	context = {
	'all_safaripackages': all_safaripackages,
	'all_categories':all_categories
	}


	return render (request, "./safaripackages/safaripackages.html", context)

def single_safaripackage(request, post_id):
	safaripackage = SafariPackages.objects.get(pk=post_id)
	day = DayNumber.objects.filter(daydetails_id = post_id)
	return render (request, './safaripackages/single_safaripackage.html', {'safaripackage':safaripackage,'day':day})
