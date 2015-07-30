from django.contrib import admin

from responses.models import Response, Petition

class PetitionInline(admin.StackedInline):
    model = Petition
    readonly_fields = ['url', 'title', 'signatures']
    can_delete = False
    extra = 0
    max_num = 0


class ResponseAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'created_at', 'total_signatures'
    ]
    list_filter = ['created_at']
    search_fields = [
        'title', 'url'
    ]
    readonly_fields = ['url']
    inlines = [PetitionInline]

admin.site.register(Response, ResponseAdmin)
admin.site.register(Petition)
