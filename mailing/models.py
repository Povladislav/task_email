from django.db import models


class MailingList(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.name
