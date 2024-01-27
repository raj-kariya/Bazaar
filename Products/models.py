from django.db import models
from django.utils.text import slugify
import datetime
import os
class Category(models.Model):
    """
    Category Model
    """
    CategoryName = models.CharField(max_length = 30)
    slug = models.SlugField(unique = True, null = True, blank = True)
    # primaryCategory = models.BooleanField(default = False)
    objects = models.Manager()
    def __str__(self):
        return str(self.CategoryName)
    def save(self , *args , **kwargs):
        self.slug = slugify(self.CategoryName)
        super(Category ,self).save(*args , **kwargs)
# Create your models here.
class Product(models.Model):
    """
    Product Model
    """
    image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=300)
    slug = models.SlugField(unique = True, null = True, blank = True)
    # productId = models.IntegerField(default = 0)
    IDforProducts = models.IntegerField(default = 0)
    # slug = models.SlugField(unique = True, null = True, blank = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE,related_name = "Products", null = True)
    # preview_text = models.TextField(max_length = 200, verbose_name = 'Preview Text')
    # detailed_text = models.TextField(max_length = 1000, verbose_name = 'Detail Text')
    description = models.TextField(max_length = 200, default="Please add the description")
    price = models.FloatField(default = 0.0)
    objects = models.Manager()
    def __str__(self):
        return str(self.name)
    
def get_filename(instance, filename):
    old_name = filename
    current_time = datetime.datetime.now().strftime('%Y%m%d%H;%M:%S')
    filename = "%s%s" % (current_time,old_name)
    return os.path.join('uploads/',filename)