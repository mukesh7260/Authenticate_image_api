from django.db import models
from PIL import Image
import uuid
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.core.files.base import ContentFile
from django.db import models
import uuid
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.core.files.base import ContentFile
from django.db import models
from django.db import models
from django.contrib.auth.models import User



class Photo(models.Model):
    thumbnails=models.ImageField(
                                upload_to='thumbnails/', blank=True ) 

    medium = models.ImageField(upload_to='medium/',blank=True)
    large = models.ImageField(upload_to='large/',blank=True) 
    grayscale = models.ImageField(blank=True)  

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.medium.path)
        img2 = Image.open(self.large.path)
        
        large_size = (1024,768*2)
        medium_size = (500,500*2)

        img.thumbnail(medium_size)
        img.save(self.medium.path)
        gray_img = img.convert("L")
        img2.thumbnail(large_size)
        img2.save(self.large.path)
        print(img2.size)
        print(img.size)
        print(gray_img)


        



             