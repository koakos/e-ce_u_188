from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.urls import reverse

# Create your models here.
class User(AbstractUser):

    is_staff = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username)

class Customer(models.Model):

    account = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    e_mail = models.EmailField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    type = (('B2B', 'B2B'), ('Retail', 'Retail'),)
    customer_type = models.CharField(max_length=15, choices=type, null=True)
    telephone = models.CharField(max_length=10, null=True)
    vat_id = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=20,null=True)
    balance = models.PositiveIntegerField(default=0, null=True)

    def __str__(self):
        return str(self.first_name) + '|' + str(self.vat_id)

    def get_absolute_url(self):
        return reverse('logger:customer-list')

    def Sales(self):
        return ', '.join([ ('[' + 'product_name: '+ str(sale.product_name) + ']') for sale in self.sales.all() ])

    def Balance(self):
        sum = 0
        for product in self.products.all():
            if product.payed == False:
                sum = sum + product.cost
        self.balance = sum
        self.save()
        return sum

    def Products(self):
        return ', '.join([ ('[' + 'product_type: '+ str(product.product_type)
        + ' device_model: '+ str(product.device_model)
        + ' issue: '+ str(product.Repairs())
        + ']') for product in self.products.all() ])

class Sale(models.Model):
    customer = models.ForeignKey(Customer,related_name='sales',on_delete=models.CASCADE)
    product_name = models.CharField(max_length=40, null=True)
    supplier = models.CharField(max_length=40, null=True)
    serial_number = models.CharField(max_length=40,null=True)
    invoice_no = models.PositiveIntegerField(default=0, null=True)
    price = models.PositiveIntegerField(default=0, null=True)
    comments = models.CharField(max_length=50, null=True)
    sale_date = models.DateTimeField(auto_now_add=True)
    warranty = models.CharField(max_length=20, null=True)

    def __str__(self):
        return str(self.customer.account.username) +'|' + str(self.product_name)

    def get_absolute_url(self):
        return reverse('logger:sales-list')


class Repair(models.Model):

    name = models.CharField(max_length=40, null=True)
    warranty = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    customer = models.ForeignKey(Customer,related_name='products',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    type = (('Notebook', 'Notebook'), ('Smartphone', 'Smartphone'),('Tablet', 'Tablet'),('Other', 'Other'),)
    product_type =  models.CharField(max_length=20, choices=type, null=True)
    device_model = models.CharField(max_length=40, null=True)
    serial_number = models.CharField(max_length=40,null=True)
    issue = models.ManyToManyField(Repair)
    damage_description = models.CharField(max_length=100,null=True)
    comment = models.CharField(max_length=100,null=True)
    cost = models.PositiveIntegerField(default=0, null=True)
    repaired = models.BooleanField(default=False)
    payed = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)

    def __str__(self):
        return str(self.customer.account.username) +' | ' + str(self.product_type) +' | ' + str(self.device_model) +' | ' + str(self.damage_description)

    def Repairs(self):
        return ', '.join([ (repair.name) for repair in self.issue.all() ])

    def Warranty(self):
        return ', '.join([ str(repair.name)+'|'+str(repair.warranty) for repair in self.issue.all() ])

    def get_absolute_url(self):
        return reverse('logger:product-detail' , kwargs ={ 'type':self.product_type,'pk': self.pk})
