

# Create your models here.
from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    extracted_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Image {self.id}"
