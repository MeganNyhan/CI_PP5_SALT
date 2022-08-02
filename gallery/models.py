import uuid
from django.db import models 
from cloudinary.models import CloudinaryField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

