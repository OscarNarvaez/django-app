from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=250)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class IdentificationType(models.Model):
    name = models.CharField(max_length=50)
    abrev = models.CharField(max_length=10)
    descrip = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class Country(models.Model):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10)
    descrip = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class Department(models.Model):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10)
    descrip = models.CharField(max_length=10)
    id_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class City(models.Model):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10)
    descrip = models.CharField(max_length=10)
    id_dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    id_ident_type = models.ForeignKey(
        IdentificationType, on_delete=models.CASCADE)
    ident_number = models.CharField(max_length=15)
    id_exp_city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=150)
    mobile = models.CharField(max_length=50)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class Student(models.Model):
    code = models.CharField(max_length=50)
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
