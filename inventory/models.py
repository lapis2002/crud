from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.
class Category (models.Model):
    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=True,blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    product_name = models.CharField(max_length=200)
    unit_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    total_quantity = models.IntegerField(default=0)
    sold = models.IntegerField(default=0, blank=True)
    category_id = models.ManyToManyField(Category)

    # Metadata
    class Meta:
        ordering = ['product_name', 'total_quantity']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('product_detail', args=[str(self.product_id)])
        
    def __str__ (self):
        return self.product_name

class Warehouse (models.Model):
    warehouse_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)
    warehouse_location = models.CharField(max_length=200)
    product_id = models.ManyToManyField(Product)
    capacity = models.IntegerField(default=1000)
    remain_capacity = models.IntegerField(default=1000)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of Warehouse."""
        return reverse('warehouse_detail', args=[str(self.warehouse_id)])

    def __str__(self):
        return f"Warehouse at %s with %d remain capacity." % self.warehouse_location, self.remain_capacity
    
class Customer (models.Model):
    customer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    customer_name = models.CharField(max_length=200)
    customer_address = models.CharField(max_length=200)
    customer_email = models.EmailField(max_length=200)
    customer_phone = models.CharField(max_length=200)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of Customer."""
        return reverse('customer_detail', args=[str(self.customer_id)])

    def __str__(self):
        return f"Customer: %s" % self.customer_name

class Supplier (models.Model):
    supplier_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    supplier_name = models.CharField(max_length=200)
    supplier_address = models.CharField(max_length=200)
    supplier_email = models.EmailField(max_length=200)
    supplier_phone = models.CharField(max_length=200)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of Supplier."""
        return reverse('supplier_detail', args=[str(self.supplier_id)])

    def __str__ (self):
        return f"Supplier: %s" % self.supplier_name

class LineItem(models.Model):
    class Status(models.TextChoices):
        process = 'PR', _('Under process')
        delivered = 'DE', _('Delivered')
        canceled = 'CA', _('Cancelled')
        received = 'RE', _('Received')
        on_hold = 'HO', _('On Hold')
        error = "ER", _('Error')

    line_item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit_price = models.DecimalField(decimal_places=2, max_digits=100.00)
    status = models.CharField(max_length=2,choices=Status.choices)

    def get_status(self) -> Status:
        return self.Status[self.status]

class Shipment (models.Model):
    class Payment(models.TextChoices):
        cash = 'CA', _('Cash')
        credit_card = 'CR', _('Credit Card')
        debit_card = "DE", _('Debit Card')

    shipment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    shipment_date = models.DateTimeField("Shipment date")
    discount = models.DecimalField(default=0, decimal_places=2, max_digits=100.00)
    line_item = models.ForeignKey(LineItem, on_delete=models.CASCADE)
    payment = models.CharField(max_length=2, choices=Payment.choices)

    def get_payment(self)->Payment:
        return self.Payment[self.payment]

class Delivery(models.Model):
    sender = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shipment = models.OneToOneField(Shipment, primary_key=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of Delivery."""
        return reverse('delivery_detail', args=[str(self.shipment)])

    def __str__ (self):
        return f"Delivery #%d" % self.shipment.shipment_id

class Receipt (models.Model):
    sender = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    shipment = models.OneToOneField(Shipment, primary_key=True,on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        """Returns the url to access a particular instance of Receipt."""
        return reverse('receipt_detail', args=[str(self.shipment)])

    def __str__ (self):
        return f"Receipt #%d" % self.shipment.shipment_id