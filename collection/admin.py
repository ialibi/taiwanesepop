from django.contrib import admin

# import your model
from collection.models import Song

# set up automated slug creation
class SongAdmin(admin.ModelAdmin):
    model = Song
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
# and register it
admin.site.register(Song, SongAdmin)