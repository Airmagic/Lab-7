from django.db import models

# Create your models here.

class Place(models.Model):
    # asking the user for these varibles
    name = models.CharField(max_length = 200)
    visited = models.BooleanField(default = False)

    # returning the infomation to the database
    def __str__(self):
        return '%s visited %s' % (self.name, self.visited)
