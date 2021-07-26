from django.db import models
from django.db.models import CharField
from django.utils.translation import gettext_lazy as _
from sodp.users.models import User


class view(models.Model):
    id = CharField(_("id"), blank=True, max_length=25, primary_key=True)
    name = CharField(_("name"), blank=True, max_length=100)
    url = CharField(_("url"), blank=True, max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="viewUser", related_name="viewUser")

    def __str__(self):
        return "%s %s %s %s" % (self.id, self.name, self.name, self.url, self.user)
