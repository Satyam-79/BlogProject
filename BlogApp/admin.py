from django.contrib import admin
from BlogApp.models import Blog,Comment

# admin.site.register(Blog)
# admin.site.register(Comment)
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_at')
    list_filter = ("status",)
    search_fields = ['title', 'detail']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, PostAdmin)