from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return str(self.name)


def upload_gallery_image(instance, filename):
    return f"images/{instance.item.name}/gallery/{filename}"


class Image(models.Model):
    image = CloudinaryField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE,
                             related_name="images")
