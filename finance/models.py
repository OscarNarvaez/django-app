from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils import timezone


class Client(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    phone = models.IntegerField(null=False, default=0)
    password = models.CharField(max_length=128, null=False, default="")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.last_name} - {self.email} - {self.phone}"


class Product(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=False)
    abbreviation = models.CharField(max_length=3, null=False)
    description = models.CharField(max_length=100, null=False, default="")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ClientProduct(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    account_number = models.IntegerField(null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.client.name} - {self.product.name}"


class Type_transaction(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    abbreviation = models.CharField(max_length=3, null=False)
    description = models.CharField(max_length=100, null=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    transaction = models.ForeignKey(
        "transaction", on_delete=models.CASCADE, null=True, blank=True, default=None
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=None)
    typeTransaction = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    amount = models.FloatField(null=False, default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} - {self.client} - {self.amount} - {self.typeTransaction}"
