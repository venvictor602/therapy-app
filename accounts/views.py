from django.contrib import messages
from product.models import Product,Category
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.
def home(request):
    
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name, email=email, subject=subject, message=message )

        contact.save()
        messages.success(request, 'Your request has been submitted, we will get back to you soon')
    return render(request,'contact.html')
