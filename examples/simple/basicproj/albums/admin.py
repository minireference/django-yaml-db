from django.contrib import admin

# Register your models here.
from .models import Album, Track


class AlbumAdmin(admin.ModelAdmin):
    pass
    
class TrackAdmin(admin.ModelAdmin):
    pass
    

admin.site.register(Album, AlbumAdmin)
admin.site.register(Track, TrackAdmin)