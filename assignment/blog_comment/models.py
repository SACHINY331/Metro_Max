from django.db import models

# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=250)
    publication_date=models.DateTimeField(auto_now_add=True)
    content=models.TextField()

    def __str__(self):
        return f"{self.title}-{self.id}"
    
class comment(models.Model):
    post=models.ForeignKey(blog,on_delete=models.CASCADE)
    content=models.TextField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)