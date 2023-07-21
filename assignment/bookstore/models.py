from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.




#creating author model
class author(models.Model):
    name=models.CharField(max_length=70)
    biography=models.TextField()
    photo= models.ImageField(upload_to='bookstore/images', default="")

    def __str__(self):
        return f"{self.name}-{self.id}"

    

    

#creating book model
class book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(author,on_delete=models.CASCADE)
    price=models.IntegerField(default=0)
    publication_date=models.DateTimeField()
    discription=models.TextField()
    image = models.ImageField(upload_to='bookstore/images', default="")

    def __str__(self):
        return f"{self.title}-{self.id}"    


class review(models.Model):
    book=models.ForeignKey(book,on_delete=models.CASCADE)
    content=models.TextField()
    rating=models.IntegerField(default=0,validators=[MaxValueValidator(10),MinValueValidator(1)])  
