from notes.models import Note, Cathegory
from django.contrib import admin


# Changes to the appearence of the admin interface
class NoteAdmin(admin.ModelAdmin):
    fieldsets = [
        # 'url', 'description', 'rating', 'cathegory'
        (None, {'fields': ['url', 'description']}),
        ('Additionla Information', {'fields': ['rating', 'cathegory']})
        ]
    list_display = ['description', 'cathegory', 'rating']
    list_filter = ['rating', 'cathegory']
    search_fields = ['description', 'url']


class NoteInline(admin.TabularInline):
    model = Note
    extra = 5


class CathegoryAdmin(admin.ModelAdmin):
    inlines = [NoteInline]
    list_display = ['label', 'description']

admin.site.register(Note, NoteAdmin)
admin.site.register(Cathegory, CathegoryAdmin)

