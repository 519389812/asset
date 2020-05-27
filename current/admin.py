from django.contrib import admin
from current.models import Current


class CurrentAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    list_display_links = ("id",)
    search_fields = ("name",)


admin.site.register(Current, CurrentAdmin)
