from django.db import models

# Create your models here.
class account(models.Model):
    account_number=models.IntegerField()
    balance=models.IntegerField()
    account_type=models.CharField(max_length=20,choices=(('saving_account','saving_account'),('current_account','current_account')))

    def __str__(self):
        return f"{self.account_number}-{self.id}"

class customer(models.Model):
    accounts=models.ManyToManyField(account,related_name='account')
    name=models.CharField(max_length=50)
    addres=models.TextField()
    phone_number=models.IntegerField()
    email=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}-{self.accounts}-{self.id}"

