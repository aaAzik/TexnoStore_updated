from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

#author = User.objects.get(id=1).id  

class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    slug = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to='category_image',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    name = models.CharField(max_length=150, null=False, blank=False)
    slug = models.CharField(max_length=150, null=False, blank=False)
    product_image = models.ImageField(upload_to='products/%Y/%m/%d/',null=True, blank=True )
    description = models.TextField(max_length=999, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-id']