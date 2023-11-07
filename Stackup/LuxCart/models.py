from PIL import Image
from django.db import models
from ckeditor.fields import RichTextField

class productlisting(models.Model):
    image=models.ImageField(upload_to='images',null=True,blank=True)
    title=models.CharField(max_length=250)
    rating=models.IntegerField(null=True,blank=True)
    description=RichTextField(null=True)
    price=models.IntegerField()
    discount=models.IntegerField()