from django.contrib import admin
from place.models import Room, Area
from django.contrib import messages
from record.models import CurrentStorage


class RoomAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "function",)
    list_display_links = ("id",)
    search_fields = ("name",)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ["id", "name"]
        else:
            return []


class AreaAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "room",)
    list_display_links = ("id",)
    search_fields = ("name",)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ["id", "name"]
        else:
            return []

    def save_model(self, request, obj, form, change):
        if change:
            if "room" in form.changed_data:
                if len(CurrentStorage.objects.filter(area_name=obj.name)) > 0:
                    messages.success(request, "检查到货架地址有变更，已更新物库存记录")
                    CurrentStorage.objects.filter(area_name=obj.name).update(room_name=obj.room.name)
        super(AreaAdmin, self).save_model(request, obj, form, change)


admin.site.register(Room, RoomAdmin)
admin.site.register(Area, AreaAdmin)