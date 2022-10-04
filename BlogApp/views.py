from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import templates
from BlogApp.forms import UserImageForm  
from BlogApp.models import UploadImage


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