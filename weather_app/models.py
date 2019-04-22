# @Date:   2019-04-21T14:32:45+06:00
# @Last modified time: 2019-04-21T15:35:46+06:00

from django.db import models

class City(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
