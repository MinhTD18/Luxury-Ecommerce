from django.db import models
from django.contrib.auth.models import User


def product_upload_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/product_<id>/<filename>
    return 'store/media/product_{0}_{1}'.format(instance.id, filename)


class TimeStampMixin(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Catalog(TimeStampMixin):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'catalog'

    def __str__(self):
        return self.name


class Product(TimeStampMixin):
    catalog = models.ForeignKey(Catalog, on_delete=models.SET_NULL, blank=True, null=True, related_name='products')

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(default=False)
    quantity = models.IntegerField()
    discount = models.FloatField(default=False, null=True)
    image_link = models.ImageField(upload_to=product_upload_path)

    class Meta:
        db_table = 'product'
        indexes = [models.Index(fields=["name", "price", "quantity", "discount"], name="product_idx")]

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)

    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)

    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)

    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
