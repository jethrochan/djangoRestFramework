from django.db import models

class Vessel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    size = models.IntegerField()
    color = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='vessels', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)
