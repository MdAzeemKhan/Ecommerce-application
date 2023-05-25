from django.db import models

# Create your models here.
class Candidate(models.Model):
    user_name=models.CharField(max_length=100)
    contact=models.IntegerField()
    image=models.ImageField(upload_to='user/image/')
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.user_name


class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE ,default=1)
    description=models.TextField(default='')
    image=models.ImageField(upload_to='product/image/')

    def __str__(self):
        return self.name