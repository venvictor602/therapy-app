from django.db import models
import secrets
from .paystack import PayStack
from product.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    book_date=models.DateField(blank=True,null=True)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, null=False)
    state=models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    verified=models.BooleanField(default=False)
    ref=models.CharField(max_length=200)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self) -> str:
        return f"Payment by :{self.email}"

    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Order.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref =ref
        super().save(*args, **kwargs)

    def amount_value(self) -> int:
        return self.amount * 100
            
    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified = True
            self.save()
            if self.verified:
                return True
            return False

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return '%s' % self.id
    
    def get_total_price(self):
        return self.price * self.quantity