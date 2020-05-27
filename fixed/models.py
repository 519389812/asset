from django.db import models
from place.models import Room


class Fixed(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=20, unique=True, verbose_name="名称")
    location = models.ForeignKey(Room, to_field="name", related_name="location", on_delete=models.DO_NOTHING,
                                 verbose_name="位置")
    status = models.CharField(max_length=6, choices=(("using", "在用"), ("idle", "闲置"), ("broken", "损坏")),
                              verbose_name="状态")

    class Meta:
        verbose_name = "管理固定资产"
        verbose_name_plural = "管理固定资产"

    def __str__(self):
        return self.name
