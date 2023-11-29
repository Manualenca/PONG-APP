from django.contrib import admin
from VentayFact.models import Campañas, Productos

# Register your models here.
class cargarCampaña(admin.ModelAdmin):
    pass
admin.site.register(Campañas)

class cargarProducto(admin.ModelAdmin):
    pass
admin.site.register(Productos)
