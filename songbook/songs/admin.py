from django.contrib import admin
from .models import Song

admin.site.site_header = 'Songbook'


# Register your models here.
admin.site.register(Song)
