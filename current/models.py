from django.db import models


class Current(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20, unique=True, verbose_name="名称")

    class Meta:
        verbose_name = "管理流动资产"
        verbose_name_plural = "管理流动资产"

    def __str__(self):
        return self.name
