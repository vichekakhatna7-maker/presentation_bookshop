from django.db import models
from django.utils import timezone
class Customer(models.Model): """Customer who buys books"""
name = models.CharField(max_length=150)
company_name = models.CharField(max_length=150, blank=True)
phone = models.CharField(max_length=20, blank=True)
email = models.EmailField(blank=True)
address = models.TextField(blank=True)

def __str__(self):
    return self.name
class Employee(models.Model): """Employee at the book shop"""
class SexChoices(models.TextChoices):
    MALE = "MALE", "Male"
    FEMALE = "FEMALE", "Female"

class MaritalStatusChoices(models.TextChoices):
    SINGLE = "SINGLE", "Single"
    MARRIED = "MARRIED", "Married"
    DIVORCED = "DIVORCED", "Divorced"

name = models.CharField(max_length=150)

sex = models.CharField(
    max_length=10,
    choices=SexChoices.choices
)

date_of_birth = models.DateField(
    blank=True,
    null=True
)

address = models.TextField(blank=True)

marital_status = models.CharField(
    max_length=10,
    choices=MaritalStatusChoices.choices,
    default=MaritalStatusChoices.SINGLE
)

have_spouse = models.BooleanField(default=False)

number_of_children = models.PositiveIntegerField(default=0)

hired_date = models.DateField(default=timezone.now)

position = models.CharField(max_length=100)

department = models.CharField(max_length=100)

def __str__(self):
    return self.name
class Item(models.Model): """Book or other item sold in the shop"""
name = models.CharField(max_length=200)

description = models.TextField(blank=True)

quantity = models.IntegerField(default=0)

sale_price = models.DecimalField(
    max_digits=10,
    decimal_places=2
)

def __str__(self):
    return f"{self.name} (${self.sale_price})"
class Sale(models.Model): """Record of each sale transaction"""
txn_number = models.CharField(
    max_length=50,
    unique=True
)

customer = models.ForeignKey(
    Customer,
    on_delete=models.CASCADE,
    related_name="sales"
)

employee = models.ForeignKey(
    Employee,
    on_delete=models.PROTECT,
    related_name="sales"
)

note = models.TextField(blank=True)

created_at = models.DateTimeField(default=timezone.now)

def __str__(self):
    return f"Sale #{self.txn_number} - {self.customer}"
class SaleDetail(models.Model): """Links an Item to a Sale with a quantity"""
sale = models.ForeignKey(
    Sale,
    on_delete=models.CASCADE,
    related_name="details"
)

item = models.ForeignKey(
    Item,
    on_delete=models.PROTECT
)

description = models.CharField(
    max_length=255,
    blank=True
)

quantity = models.PositiveIntegerField(default=1)

price = models.DecimalField(
    max_digits=10,
    decimal_places=2
)

def subtotal(self):
    return self.quantity * self.price

def __str__(self):
    return f"{self.quantity} x {self.item.name}"