from django.contrib import admin

# Register your models here.

from .models import Blogpost


class BlogpostAdmin(admin.ModelAdmin):
    exclude = ['posted']
    # prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author')


admin.site.register(Blogpost, BlogpostAdmin)
