from django.db import models

# Create your models here.
from django.db import models

class ImageModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='images/')
    file_size = models.CharField(max_length=50, blank=True, editable=False)  # Field for image size
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Automatically calculate the file size before saving
        if self.image and hasattr(self.image, 'size'):
            size_in_kb = self.image.size / 1024  # Convert to KB
            if size_in_kb > 1024:
                self.file_size = f"{size_in_kb / 1024:.2f} MB"  # Convert to MB if larger than 1 MB
            else:
                self.file_size = f"{size_in_kb:.2f} KB"
        else:
            self.file_size = "0 KB"  # Default value if no image

        super().save(*args, **kwargs)