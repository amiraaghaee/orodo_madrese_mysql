from django.db import models
from django.contrib.auth.models import User


# class User(models.Model):
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)

class Product(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    inventory = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.name

    def increase_inventory(self, amount):
        pass

    def decrease_inventory(self, amount):
        pass


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    balance = models.IntegerField()

    def __str__(self):
        return self.user

    def deposit(self, amount):
        pass

    def spend(self, amount):
        pass


class OrderRow(models.Model):
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    order = models.ForeignKey('Order', on_delete=models.PROTECT)
    amount = models.IntegerField()


class Order(models.Model):
    # Status values. DO NOT EDIT
    STATUS_SHOPPING = 1
    STATUS_SUBMITTED = 2
    STATUS_CANCELED = 3
    STATUS_SENT = 4

    customer = models.ForeignKey('Customer', on_delete=models.PROTECT)
    order_time = models.DateTimeField()
    total_price = models.IntegerField()
    status_choices = (
        (STATUS_SHOPPING, 'در حال خرید'),
        (STATUS_SUBMITTED, 'ثبت شده'),
        (STATUS_CANCELED, 'لغو شده'),
        (STATUS_SENT, 'ارسال شده'),

    )
    status = models.IntegerField(choices=status_choices)

    @staticmethod
    def initiate(customer):
        return models.ForeignKey('Order', on_delete=models.PROTECT)

    def add_product(self, product, amount):
        pass

    def remove_product(self, product, amount=None):
        pass

    def submit(self):
        pass

    def cancel(self):
        pass

    def send(self):
        pass
