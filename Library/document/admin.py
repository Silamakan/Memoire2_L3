from django.contrib import admin
from .models import Domaine, Ouvrage

# Register your models here.
class DomaineAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class OuvrageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titre',)}

admin.site.register(Domaine, DomaineAdmin)
admin.site.register(Ouvrage, OuvrageAdmin)

