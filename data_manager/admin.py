from django.contrib import admin
from .models import Erabiltzailea

# Register your models here.
from data_manager.models import Erabiltzailea, Taldea, Estropada, Egutegia, Gremioa, Kiniela


class ErabiltzaileaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Taldea, ErabiltzaileaAdmin)
admin.site.register(Estropada, ErabiltzaileaAdmin)
admin.site.register(Egutegia, ErabiltzaileaAdmin)
admin.site.register(Gremioa, ErabiltzaileaAdmin)
admin.site.register(Erabiltzailea, ErabiltzaileaAdmin)
admin.site.register(Kiniela, ErabiltzaileaAdmin)
