from django.db import models


class Room(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=20, unique=True, verbose_name="名称")
    function = models.CharField(max_length=10, choices=(("office", "办公室"), ("warehouse", "仓库")), verbose_name="用途")

    class Meta:
        verbose_name = "管理办公室及仓库"
        verbose_name_plural = "管理办公室及仓库"

    def __str__(self):
        return self.name


class Area(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=20, unique=True, verbose_name="名称")
    room = models.ForeignKey(Room, to_field="name", related_name="room", on_delete=models.DO_NOTHING,
                             verbose_name="所在位置")

    class Meta:
        verbose_name = "管理货架"
        verbose_name_plural = "管理货架"

    def __str__(self):
        return self.name
