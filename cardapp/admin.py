from django.contrib import admin
from .models import CardModel


class CardAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


# Register your models here.
admin.site.register(CardModel, CardAdmin)
