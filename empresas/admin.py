from django.contrib import admin

# Register your models here.
from .models import Empresa


class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("cod_empresa", "nome")


admin.site.register(Empresa, EmpresaAdmin)
