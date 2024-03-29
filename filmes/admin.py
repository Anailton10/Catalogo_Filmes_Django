from django.contrib import admin
from .models import FilmRegistration, Category


class FilmAdmin(admin.ModelAdmin):
    list_play = ('title', 'category', 'duration', 'author')
    search_fields = ('title', 'category')


admin.site.register(FilmRegistration, FilmAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
