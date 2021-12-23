from django.db import models


class Product(models.Model):
    picture = models.ImageField(upload_to='app/static/app/uploads/img/products/')
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    code = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)


class Member(models.Model):
    picture = models.ImageField(upload_to='app/static/app/uploads/img/members/')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=7)
    club_member_number = models.PositiveIntegerField()
    date_of_issue_vog = models.DateField()
    knsa_member_number = models.PositiveIntegerField()
    shooting_count = models.PositiveIntegerField()
    member_since = models.DateField()
    category = models.CharField(max_length=50)
