from django.contrib import admin
from fixed.models import Fixed


class FixedAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "location",)
    list_display_links = ("id",)
    search_fields = ("name", "location__name",)


admin.site.register(Fixed, FixedAdmin)
