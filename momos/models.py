# Create your models here.

import uuid

from django.db import models
from django.contrib.auth.models import User


def generate_uuid():
    return uuid.uuid4().hex


class base (models.Model):
    reference_id = models.CharField(
        max_length=32, unique=True, primary_key=True, default=generate_uuid)
    is_delete = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, db_column="created_by", on_delete=models.PROTECT, related_name='+')
    created_at = models.DateTimeField()
    updated_by = models.ForeignKey(
        User, db_column="updated_by", on_delete=models.PROTECT, null=True)
    Updated_at = models.DateField(null=True)

    class Meta:
        abstract = True


class momomessage(base):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    select = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    countrycode = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=10)
    msg = models.CharField(max_length=200)

    class Meta:
        db_table = "momomessage"

    def _str_(self):
        return self.email
