from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.

class UserTask(models.Model):
    user = models.ForeignKey(to=User, verbose_name=_('User'), db_index=True, on_delete=models.CASCADE,
                             related_name='my_tasks')
    name = models.CharField(verbose_name=_('Task name'), db_index=True, max_length=255)
    description = models.TextField(verbose_name=_('Description'))
    date_create = models.DateTimeField(auto_now_add=True, verbose_name=_('Date create'))
    date_update = models.DateTimeField(auto_now=True, verbose_name=_('Date update'))
    archive = models.BooleanField(verbose_name=_('Completed'), default=0)

    class Meta:
        db_table = 'DJ_user_task'
        ordering = ['-date_update', '-date_create']
        verbose_name = _('UserTask')
        verbose_name_plural = _('UserTasks')
