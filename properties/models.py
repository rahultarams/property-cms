from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.contrib.auth.models import User
# Create your models here.


class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    # Assuming location implies a geographical coordinate, we could use latitude and longitude
    #latitude = models.DecimalField(max_digits=9, decimal_places=6)
    #longitude = models.DecimalField(max_digits=9, decimal_places=6)
    posted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='your_models',
        null=True,  # Temporarily allow null
        blank=True
    )

    def __str__(self):
        return self.name

class PropertyPluginModel(CMSPlugin):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="plugins")

    def __str__(self):
        return self.property.name