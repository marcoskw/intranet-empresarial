from django.contrib import admin
from .models import Colaborador, Setor, Cargo


class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'setor', 'cargo', 'ramal', 'email', 'data_aniversario', 'status')
    list_display_links = ('id', 'nome')
    list_editable = ('status',)
    search_fields = ('id', 'nome', 'setor', 'cargo', 'ramal', 'email', 'data_aniversario', 'status')


class SetorAdmin(admin.ModelAdmin):
    list_display = ('id', 'setor')
    list_display_links = ('id', 'setor')


class CargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cargo')
    list_display_links = ('id', 'cargo')


admin.site.register(Setor, SetorAdmin)
admin.site.register(Cargo, CargoAdmin)
admin.site.register(Colaborador, ColaboradorAdmin)
