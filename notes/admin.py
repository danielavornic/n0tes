from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Note, NoteAdmin)