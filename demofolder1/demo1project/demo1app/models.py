from django.db import models

# Create your models here.
class places(models.Model):
    pname=models.CharField(max_length=50)
    img=models.ImageField(upload_to='')
    des=models.TextField()
    # price= models.DecimalField(max_digits=10, decimal_places=2)


class team(models.Model):
    tname=models.CharField(max_length=50)
    pict=models.ImageField(upload_to='')
    desc=models.TextField()


    def __str__(self):
        return self.pname
    def __str__(self):
        return self.tname