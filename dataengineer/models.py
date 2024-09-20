from django.db import models

# Create your models here.
from django.db import models

class ImageModel(models.Model):
    name = models.CharField(max_length=255)  
    image = models.ImageField(upload_to='images/') 
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
