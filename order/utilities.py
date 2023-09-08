from django.conf import settings
from cart.cart import Cart
from .models import Order, OrderItem

def checkout(request, first_name, last_name, email, address, country,book_date, state, phone):
    order = Order.objects.create(first_name=first_name, last_name=last_name, email=email, address=address, book_date=book_date, state=state, phone=phone,country=country)

    for item in Cart(request):
        OrderItem.objects.create(order=order, product=item['product'], price=item['product'].price, quantity=item['quantity'])
    
        # order.add(item['product'])

    return order