from os import name
from django.db import models
# Create your models here.
class users(models.Model):
    name = models.CharField(max_length=100, null=False)
    id = models.IntegerField(primary_key=True, null=False)
    email = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)
    status = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    update_at = models.DateTimeField(auto_now=True, null=False)
    deleted_at = models.DateTimeField(auto_now=True, null=True)
    def _str_(self):
        return self.name

class students(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    code = models.CharField(max_length=50, null=False)
    id_person = models.ForeignKey('persons', on_delete=models.CASCADE)
    status = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=False)
    deleted_at = models.DateTimeField(auto_now=True, null=True)
    def _str_(self):
        return str(self.id_person)

class identification_types(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=50, null=False)
    abrev = models.CharField(max_length=10, null=False)
    descrip = models.CharField(max_length=100,null=False)
    created_at = models.DateTimeField(auto_now_add=True ,null=False)
    update_at = models.DateTimeField(auto_now=True,null=False)
    deleted_at = models.DateTimeField(auto_now=True, null=True)
    def _str_(self):
        return self.name

class countries(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=False)
    abrev = models.CharField(max_length=10, null=False)
    descrip = models.CharField(max_length=10, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    deleted_at = models.DateTimeField(auto_now=True, null=True)
    def _str_(self):
        return self.name


class departments(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=False)
    abrev = models.CharField(max_length=10, null=False)
    descrip = models.CharField(max_length=10, null=False)
    id_country = models.ForeignKey('countries', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    deleted_at = models.DateTimeField(auto_now=True, null=True)
    def _str_(self):
        return self.name

class cities(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=False)
    abrev = models.CharField(max_length=10, null=False)
    descrip = models.CharField(max_length=10, null=False)
    id_dept = models.IntegerField(null=False), models.ForeignKey('departments',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    deleted_at = models.DateTimeField(auto_now=True, null=True)
    def _str_(self):
        return self.name

class persons(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    id_ident_type = models.IntegerField(null=False), models.ForeignKey('identification_types',on_delete=models.CASCADE)
    ident_number = models.CharField(max_length=15, null=False)
    id_exp_city = models.IntegerField(null=False), models.ForeignKey('cities',on_delete=models.CASCADE)
    address = models.CharField(max_length=150, null=False)
    mobile = models.CharField(max_length=50, null=False)
    id_user = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    deleted_at = models.DateTimeField(auto_now=True, null=True)
    def _str_(self):
        return self.first_name