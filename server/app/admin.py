from django.contrib import admin
from .models import Category, Award, Nominee

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug')
    # prepopulated_fields = {'slug': ('name',)}

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'slug')
    # prepopulated_fields = {'slug': ('name',)}

@admin.register(Nominee)
class NomineeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'award', 'email', 'phone', 'slug')
    # prepopulated_fields = {'slug': ('full_name',)}

