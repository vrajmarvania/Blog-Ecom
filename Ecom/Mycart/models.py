from django.db import models

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category= models.CharField(max_length=50,default='')
    sub_category=models.CharField(max_length=50,default='')
    price=models.IntgerField(default=0)

    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="Mycart/images",default="")

    def __str__(self):
        return self.product_name


class Contect(models.Model):

    id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=40,default='')
    Email=models.CharField(max_length=40,default='')
    Phone=models.CharField(max_length=12,default='')

    N_help=models.CharField(max_length=100,default='')

    def __str__(self):
        return self.Name
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    Name = models.CharField(max_length=400, default='')
    Email = models.CharField(max_length=400, default='')
    Address = models.CharField(max_length=400, default='')
    City = models.CharField(max_length=400, default='')
    State = models.CharField(max_length=400, default='')
    Zip = models.CharField(max_length=400, default='')
    Phone = models.CharField(max_length=400, default='')

class Orderupdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:9]+"..."