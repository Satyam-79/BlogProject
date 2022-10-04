from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homePage),
    path('about/', views.aboutPage),
    path('image_upload', views.image_request, name = 'image_upload'),
    path('success', views.success, name = 'success'),
    path('admin/', views.success, name = 'success'),
    
]
