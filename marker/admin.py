from django.contrib import admin
from marker.models import Marker

class MarkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')

admin.site.register(Marker, MarkerAdmin)
