from django.contrib import admin
from record.models import CurrentRecord, CurrentStorage
from django.contrib import messages


class CurrentRecordAdmin(admin.ModelAdmin):
    list_display = (
        "id", "current_name", "quantity", "in_out", "area_name", "operation_datetime", "operation_username", "comment")
    list_display_links = ("id",)
    search_fields = ("current_name__name", "quantity", "in_out", "area_name__name",)
    fieldsets = (
        ("基本信息", {"fields": ["current_name", "quantity", "in_out", "area_name", "comment"]}),
        ("操作信息", {"fields": ["id", "operation_datetime", "operation_username"]}),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ["id", "current_name", "quantity", "in_out", "area_name", "operation_datetime", "operation_username"]
        else:
            return ["id", "operation_datetime", "operation_username"]

    def save_model(self, request, obj, form, change):
        try:
            storage_record = CurrentStorage.objects.get(current_name=obj.current_name.name, area_name=obj.area_name)
        except:
            storage_record = None
        if storage_record is not None:
            if obj.in_out == "in":
                storage_record.quantity = storage_record.quantity + obj.quantity
                storage_record.save()
                obj.operation_username = request.user.full_name
                super(CurrentRecordAdmin, self).save_model(request, obj, form, change)
            elif obj.in_out == "out":
                quantity = storage_record.quantity - obj.quantity
                if quantity < 0:
                    messages.set_level(request, level=messages.ERROR)
                    messages.error(request, "错误！出库数量大于库存数。")
                else:
                    storage_record.quantity = quantity
                    storage_record.save()
                    obj.operation_username = request.user.full_name
                    super(CurrentRecordAdmin, self).save_model(request, obj, form, change)
        else:
            if obj.in_out == "in":
                CurrentStorage.objects.create(current_name=obj.current_name.name, room_name=obj.area_name.room.name,
                                              area_name=obj.area_name.name, quantity=obj.quantity)
                obj.operation_username = request.user.full_name
                super(CurrentRecordAdmin, self).save_model(request, obj, form, change)
            elif obj.in_out == "out":
                messages.set_level(request, level=messages.ERROR)
                messages.error(request, "错误！该物资无库存记录。")


class CurrentStorageAdmin(admin.ModelAdmin):
    list_display = ("id", "current_name", "room_name", "area_name", "quantity",)
    search_fields = ("current_name", "room_name", "area_name", "quantity",)
    list_filter = ("current_name", "room_name", "area_name", "quantity",)
    ordering = ("current_name",)


admin.site.register(CurrentRecord, CurrentRecordAdmin)
admin.site.register(CurrentStorage, CurrentStorageAdmin)
