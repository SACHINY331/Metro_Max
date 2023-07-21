from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.




#creating author model
class shipment(models.Model):
    origin=models.CharField(max_length=70)
    destination=models.CharField(max_length=70)
    expected_delivery_date=models.DateTimeField()
    actual_delivery_date=models.DateTimeField()
    status=models.CharField(max_length=20,choices=(('early','early'),('delayed','delayed'),('on-time','on-time')))


#creating book model
class cargo(models.Model):
    shipment=models.ForeignKey(shipment,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    quantity=models.IntegerField()

    def __str__(self):
        return f"{self.name}-{self.id}"    


class tracking(models.Model):
    shipment=models.OneToOneField(shipment,on_delete=models.CASCADE)
    status=models.CharField(max_length=70,choices=(('packing','packing'),('arrived_at','arrivedat'),('dispatched_from','dispatched_from'),('delivered','delivered')))
    location=models.CharField(max_length=70)
