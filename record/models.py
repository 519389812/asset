from django.db import models
from current.models import Current
from place.models import Area


class CurrentRecord(models.Model):
    id = models.AutoField(primary_key=True)
    current_name = models.ForeignKey(Current, to_field="name", related_name="current_name", on_delete=models.DO_NOTHING,
                                     verbose_name="名称")
    quantity = models.IntegerField(verbose_name="数量")
    area_name = models.ForeignKey(Area, to_field="name", related_name="area_name", on_delete=models.DO_NOTHING,
                                  verbose_name="所在位置")
    in_out = models.CharField(max_length=6, choices=(("in", "入库"), ("out", "出库")), verbose_name="出入库")
    operation_datetime = models.DateTimeField(auto_now=True, verbose_name="操作时间")
    operation_username = models.CharField(max_length=16, verbose_name="操作人")
    comment = models.TextField(max_length=200, blank=True, verbose_name="备注")

    class Meta:
        verbose_name = "流动资产入出库记录"
        verbose_name_plural = "流动资产入出库记录"

    def __str__(self):
        return self.current_name.name


class CurrentStorage(models.Model):
    id = models.AutoField(primary_key=True)
    current_name = models.CharField(max_length=20, verbose_name="物资名称")
    room_name = models.CharField(max_length=20, verbose_name="所在房间")
    area_name = models.CharField(max_length=20, verbose_name="所在位置")
    quantity = models.IntegerField(verbose_name="库存数量")

    class Meta:
        verbose_name = "流动资产库存"
        verbose_name_plural = "流动资产库存"

    def __str__(self):
        return self.current_name
