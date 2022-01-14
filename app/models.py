from django.db import models


class Product(models.Model):
    active = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='app/static/app/uploads/img/products/')
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100, null=True, blank=True)
    code = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def clean(self):
        self.name = self.name.title()
        if self.description:
            self.description = self.description.capitalize()


class Member(models.Model):
    active = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='app/static/app/uploads/img/members/')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=6, null=True, blank=True)
    club_member_number = models.PositiveIntegerField()
    date_of_issue_vog = models.DateField(null=True, blank=True)
    knsa_member_number = models.PositiveIntegerField(null=True, blank=True)
    shooting_count = models.PositiveIntegerField()
    member_since = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=2)

    def clean(self):
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        if self.address:
            self.address = self.address.capitalize()
        if self.city:
            self.city = self.city.capitalize()
        if self.postal_code:
            self.postal_code = self.postal_code.upper()


class MemberPresence(models.Model):
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    is_present = models.BooleanField(default=True)


class Order(models.Model):
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    payment_method = models.PositiveIntegerField(null=True, blank=True)
    paid = models.BooleanField(default=False)


class OrderProduct(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_picture_url = models.CharField(max_length=500)
    product_name = models.CharField(max_length=50)
    product_description = models.TextField(max_length=100, null=True, blank=True)
    product_code = models.PositiveIntegerField()
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
