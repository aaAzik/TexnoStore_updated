from django.db import models

class Category(models.Model):
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to='category_image',null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    product_image = models.ImageField(upload_to='products/%Y/%m/%d/',null=True, blank=True )
    description = models.TextField(max_length=999, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name