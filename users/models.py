from django.db import models

# class Category(models.Model):
#     title = models.CharField(max_length = 30)
#     primaryCategory = models.BooleanField(default = False)
#     def __str__(self):
#         return str(self.title)
# # Create your models here.
# class Product(models.Model):
#     mainimage = models.ImageField(upload_to='products/', blank = True)
#     name = models.CharField(max_length=300)
#     slug = models.SlugField()
#     category = models.ForeignKey(Category, on_delete = models.CASCADE)
#     preview_text = models.TextField(max_length = 200, verbose_name = 'Preview Text')
#     detailed_text = models.TextField(max_length = 1000, verbose_name = 'Detail Text')
#     price = models.FloatField()


#     def __str__(self):
#         return str(self.name)