from django.db import models


class SignatureVistor(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.email
