from django.db import models

# Create your models here.

#creating product model
class product(models.Model):
    name=models.CharField(max_length=70)
    description=models.TextField(max_length=250)
    price=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}-{self.id}"


#creating category model
class category(models.Model):
    name=models.CharField(max_length=70)
    product=models.ManyToManyField(product)
