from django.contrib import admin

# Register your models here.
from Andou_Kay.models import Utilisateur, Proprietaire

admin.site.register(Utilisateur)
admin.site.register(Proprietaire)