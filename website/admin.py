from django.contrib import admin
from .models import Record
from .models import Event
# Register your models here.
admin.site.register(Record)


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'start_time', 'end_time', 'start_hour', 'end_hour']
    list_filter = ['start_time', 'end_time']
    search_fields = ['title', 'description']
    date_hierarchy = 'start_time'  # Opcional, para facilitar la navegación por fechas

admin.site.register(Event, EventAdmin)
