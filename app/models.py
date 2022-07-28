from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_no = models.IntegerField()
    city = models.CharField(max_length=100)
    manager_name = models.CharField(max_length=100)
