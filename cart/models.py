from email.policy import default
from django.db import models
from django.contrib.auth import get_user
from Products.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'

    def __str__(self) -> str:
        return f'{self.quantity} of {self.item.name}'
    
    def get_total(self):
        total = self.item.price*self.quantity
        floatTotal = float("{0:.2f}".format(total))
        return floatTotal

# class Order(models.Model):
#     orderItems = models.ManyToManyField(Cart)
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     ordered = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add = True)
#     paymentId = models.CharField(max_length = 200,blank = True,null = True)
#     orderId = models.CharField(max_length = 200,blank = True,null = True) 