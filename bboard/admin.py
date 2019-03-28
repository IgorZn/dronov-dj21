from django.contrib import admin
from .models import db, Rubric

# Register your models here.
class DBAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')



admin.site.register(db, DBAdmin)
admin.site.register(Rubric)