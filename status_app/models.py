from django.db import models


class Status(models.Model):
    stage = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return self.stage
