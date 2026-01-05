# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    ext_int = models.IntegerField(null=True, blank=True)
    ext_str = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Tbl_Rt(models.Model):

    #__Tbl_Rt_FIELDS__
    tagname = models.TextField(max_length=255, null=True, blank=True)
    int_v = models.IntegerField(null=True, blank=True)
    alias = models.TextField(max_length=255, null=True, blank=True)
    bool_v = models.BooleanField()
    dt_v = models.DateTimeField(blank=True, null=True, default=timezone.now)
    str_v = models.TextField(max_length=255, null=True, blank=True)

    #__Tbl_Rt_FIELDS__END

    class Meta:
        verbose_name        = _("Tbl_Rt")
        verbose_name_plural = _("Tbl_Rt")


class Tbl_Set(models.Model):

    #__Tbl_Set_FIELDS__
    tagname = models.TextField(max_length=255, null=True, blank=True)
    int_set = models.IntegerField(null=True, blank=True)
    str_set = models.TextField(max_length=255, null=True, blank=True)
    int_val = models.IntegerField(null=True, blank=True)
    str_val = models.TextField(max_length=255, null=True, blank=True)
    update = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Tbl_Set_FIELDS__END

    class Meta:
        verbose_name        = _("Tbl_Set")
        verbose_name_plural = _("Tbl_Set")



#__MODELS__END
