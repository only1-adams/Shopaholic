from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from home.models import *
from product.models import *
from .models import *
from user.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# import requests
import json
import random
import string
import uuid
from django.views.decorators.http import require_POST

# Create your views here.


def order(request):
    return HttpResponse('e good')

@require_POST
@login_required(login_url='/login')
def addtoshopcart(request):
    url = request.META.get('HTTP_REFERER')
    thequantity = int(request.POST['quantity'])
    thecolor = request.POST.get('color', None)
    theprodid = request.POST['prodid']
    aprod = Product.objects.get(pk=theprodid)

    cart= ShopCart.objects.filter(order_placed=False).filter(user__username=request.user.username)

    if cart: #an existing cart is noticed 
        prodchecker = ShopCart.objects.filter(product_id = aprod.id, color=thecolor, quantity=thequantity,user__username=request.user.username).first()

        if prodchecker: #product exists in the cart increment it
            prodchecker.quantity += thequantity
            prodchecker.color = thecolor
            prodchecker.save()
            messages.success(request, "Product added to Shopcart")
            return redirect(url)

        else: #product is not in cart add it
            anitem = ShopCart()
            anitem.product=aprod
            anitem.user=request.user
            anitem.order_code=cart[0].order_code
            anitem.quantity=thequantity
            anitem.color=thecolor
            anitem.order_placed=False
            anitem.save()
    
    else: #create a new cart,  generate order code
         ordercode = str(uuid.uuid4())
         newcart = ShopCart()
         newcart.product =aprod
         newcart.user =request.user
         newcart.order_code=ordercode
         newcart.quantity=thequantity
         newcart.color=thecolor 
         newcart.order_placed-False
         newcart.save()
    
    messages.success(request, "Product added to Shopcart")

    return redirect(url)

@login_required(login_url='/login')
def shopcart(request):

    profile= Profile.objects.get(pk=1)
    category = Category.objects.all()
    shopcart = ShopCart.objects.filter(order_placed=False).filter(user__username=request.user.username)

    Subtotal=0
    Shippingfee=0
    vat=0
    total=0

    for item in shopcart:
        if item.product.discount_price:
            Subtotal += item.product.discount_price * item.quantity
        else:
            Subtotal += item.product_price *  item.quantity

    # Shipping rules: 8% fees to all orders above 450.0 fees to orders lower
    if Subtotal > 450:
        Shippingfee = 0.09 * Subtotal
    else:
        Shippingfee=0

    vat = 0.085 * Subtotal

    total = Subtotal + Shippingfee + vat

    context ={
        'profile': profile,
        'category': category,
        'shopcart': shopcart,
        'Shipping': Shippingfee,
        'Subtotal': Subtotal,
        'vat': vat,
        'total': total
    }
    
    return render(request,'shopcart.html', context)

@require_POST
@login_required(login_url='/login')
def updatequantity(request):
    url = request.META.get('HTTP_REFERER')
    newquantity = request.POST['itemquan']
    theitem = ShopCart.objects.get(id=request.POST ['itemid'])
    theitem.quantity = newquantity
    theitem.save()

    messages.success(request, "Product Quantity successfully updated")
    return redirect(url)

@login_required(login_url='/login')
def deletefromcart(request,id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, "Item deleted from Shopcart.")
    return redirect('order:shopcart')