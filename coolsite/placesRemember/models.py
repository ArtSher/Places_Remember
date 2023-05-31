from django.db import models



class Remember(models.Model):
    address = models.CharField(max_length=200, null=True)
    comment = models.TextField()

    def __str__(self):
        return self.address