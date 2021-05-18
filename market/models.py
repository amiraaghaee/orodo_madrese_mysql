from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    balance = models.IntegerField()


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


class OrderRow(models.Model):
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    order = models.ForeignKey('Order', on_delete=models.PROTECT)
    amount = models.IntegerField(null=True)


class Order(models.Model):
    # Status values. DO NOT EDIT
    STATUS_SHOPPING = 1
    STATUS_SUBMITTED = 2
    STATUS_CANCELED = 3
    STATUS_SENT = 4
    #
    # customer = models.ForeignKey('User', on_delete=models.PROTECT)
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
    def initiate(user):
        return models.ForeignKey('Order', on_delete=models.PROTECT)

    @staticmethod
    def add_product(product, amount):
        product.inventory += amount
        if product.inventory >= 0:
            product.save()

    def remove_product(self, product, amount=None):
        pass

    def submit(self):
        pass

    def cancel(self):
        pass

    def send(self):
        pass
