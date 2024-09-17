from django.db import models

# Create your models here.
from django.db import models

class ImageModel(models.Model):
    name = models.CharField(max_length=255)  # Field to store the name
    image = models.ImageField(upload_to='images/')  # Field to store the image

    def __str__(self):
        return self.name
