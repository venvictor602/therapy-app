from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect,render
from django.conf import settings
from order.models import Order
from django.contrib import messages
from .cart import Cart
from .forms import CheckoutForm
from order.utilities import checkout


def cart_detail(request: HttpRequest) -> HttpResponse:
    cart = Cart(request)
                           
    remove_from_cart = request.GET.get('remove_from_cart', '')
    change_quantity = request.GET.get('change_quantity', '')
    quantity = request.GET.get('quantity', 0)

    if remove_from_cart:
        cart.remove(remove_from_cart)

        return redirect('cart')
    
    if change_quantity:
        cart.add(change_quantity, quantity, True)

        return redirect('cart')
    return render(request, 'cart.html')


def verify_payment(request: HttpRequest, ref:str) -> HttpResponse:
    cart = Cart(request)
    payment = get_object_or_404(Order, ref=ref)
    if request.method == 'POST':
        cart.clear()
    else:
        cart.clear()
    return render(request,'success.html')

def success(request):
    cart = Cart(request)
    if request.method == 'POST':
        cart.clear()
    else:
        cart.clear()
    return render(request,'success.html')

def checkup(request):
    cart = Cart(request)
    form = CheckoutForm()
    if request.method == 'POST':
        form=CheckoutForm(request.POST)

        if form.is_valid():
            if request.method == 'POST':
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                address = form.cleaned_data['address']
                state = form.cleaned_data['state']
                book_date=form.cleaned_data['book_date']
                country=form.cleaned_data['country']
                order = checkout(request,first_name=first_name, last_name=last_name, email=email, address=address, state=state, phone=phone, book_date=book_date,country=country)
                form = form.save()
                
                return render(request,'make_payment.html',{'form':form,'paystack_public_key':settings.PAYSTACK_PUBLIC_KEY})
    return render(request,'checkup.html')