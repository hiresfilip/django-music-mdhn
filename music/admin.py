from django.contrib import admin
from django.db.models import Count

from .models import *

#admin.site.register(Type)
# Registrace modelů v admin rozhraní
@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ("name", "instrument_count")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _instrument_count=Count("instrument", distinct=True),
        )
        return queryset

    def instrument_count(self, obj):
        return obj._instrument_count

    instrument_count.admin_order_field = "_instrument_count"
    instrument_count.short_description = "Number of Instruments"


#admin.site.register(Instrument)

@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    list_display = ("title", "count_types")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _type_count=Count("type", distinct=True),
        )
        return queryset

    def count_types(self, obj):
        return obj._type_count

    count_types.short_description = "Number of types"



#admin.site.register(Attachment)

@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "filesize", "instrument_type")

    def instrument_type(self, obj):
        return obj.instrument.title