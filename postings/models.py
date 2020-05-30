from django.conf import settings
from django.db import models
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse


# django hosts --> subdomain for reverse

class myAdmin(models.Model):
    # pk aka id --> numbers
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, null=True, blank=True)
    email = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(max_length=120, null=True, blank=True)

    def __str__(self):
        return str(self.name)


    # def __str__(self):
    #     return str(self.user.username)
