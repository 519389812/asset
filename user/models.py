from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    full_name = models.CharField(max_length=16, verbose_name="全名")

    class Meta:
        verbose_name = "管理用户"
        verbose_name_plural = "管理用户"

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        self.full_name = self.last_name + self.first_name
        super(User, self).save(*args, **kwargs)
