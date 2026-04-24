from django.contrib import admin
from .models import Film

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "year"]
    search_fields = ["title", "year"]
    list_filter = ["title", "year"]
