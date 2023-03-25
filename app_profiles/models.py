from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Profile(models.Model):
    STATUS_CHOISES = (
        ('be', 'beginner'),
        ('ad', 'advanced'),
        ('ex', 'expert')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, verbose_name=_('name'))
    last_name = models.CharField(max_length=20, verbose_name=_('last_name'))
    date_of_birthday = models.DateField(verbose_name=_('date_of_birthday'))
    balance = models.PositiveIntegerField(verbose_name=_('balance'), default=0)
    status = models.CharField(max_length=2, choices=STATUS_CHOISES, default=STATUS_CHOISES[0], verbose_name=_('status'))
    spent_balance = models.PositiveIntegerField(verbose_name=_('spent balance'), default=0)

    class Meta:
        verbose_name = _('Профиль')
        verbose_name_plural = _('Профили')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

