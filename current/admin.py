from django.contrib import admin
from current.models import Current


class CurrentAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    list_display_links = ("id",)
    search_fields = ("name",)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ["id", "name"]
        else:
            return []


admin.site.register(Current, CurrentAdmin)
