from django.contrib import admin
from .models import *
# Register your models here
class Blog_files_tables(admin.TabularInline):
    model = ProductImage
class blog_admin(admin.ModelAdmin):
    inlines = [Blog_files_tables]
admin.site.register(Blog,blog_admin)
admin.site.register(ProductImage)
admin.site.register(Teachers)
admin.site.register(Comment)
admin.site.register(Books)
admin.site.register(sinf)
admin.site.register(Javob)