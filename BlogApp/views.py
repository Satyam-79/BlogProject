from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import templates
from BlogApp.forms import UserImageForm,NewUserForm
from BlogApp.models import UploadImage
from django.contrib.auth import login
from django.contrib import messages


def homePage(request):
    return render(request, "index.html")

def aboutPage(request):
    return render(request, "about.html")

def image_request(request):
  
    if request.method == 'POST':
        form = UserImageForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserImageForm()
    return render(request, 'image_form.html', {'form' : form})
  
  
def success(request):
    return HttpResponse('successfully uploaded')

def blogPage(request):
    return render(request, "blog.html")

def contactPage(request):
    return render(request, "contact.html")

def detailPage(request):
    return render(request, "detail.html")

def featurePage(request):
    return render(request, "feature.html")

def pricePage(request):
    return render(request, "price.html")

def quotePage(request):
    return render(request, "quote.html")

def servicePage(request):
    return render(request, "service.html")

def teamPage(request):
    return render(request, "team.html")

def testimonialPage(request):
    return render(request, "testimonial.html")


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			# return redirect("homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})