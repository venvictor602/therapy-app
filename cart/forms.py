from django import forms
from order.models import Order


class CheckoutForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=("first_name","last_name","address","country","book_date","state","phone","email",)