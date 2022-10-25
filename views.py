from multiprocessing import context
from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from requests import request
from .models import *
# Create your views here.
def product(request):
      if request.user.is_authenticated:
            customer=request.user.customer
            order, created=Order.objects.get_or_create(customer=customer,complete=False)
            items=order.orderitem_set.all()
            cartItems=order.get_cart_items
      else:
            items=[]
            order={'get_cart_total':0,'get_cart_items':0}
            cartItems=order['get_cart_items']
      products=Product.objects.all()
      context = {'products':products,'cartItems':cartItems}
      return render(request, 'store/Products.html', context)
 
def cart(request):
      if request.user.is_authenticated:
            customer=request.user.customer
            order, created=Order.objects.get_or_create(customer=customer,complete=False)
            items=order.orderitem_set.all()
      else:
            items=[]
            order={'get_cart_total':0,'get_cart_items':0}
      context = {'items':items, 'order':order}
      return render(request, 'store/cart.html', context)

def contact(request):
	context = {}
	return render(request, 'store/contact.html', context)
def sp(request):
      sproducts=Sproduct.objects.all()
      context = {'sproducts':sproducts}
      return render(request, 'store/sproduct.html', context)
def sp1(request):
      context = {}
      return render(request, 'store/sproduct1.html', context)
def sp2(request):
      context = {}
      return render(request, 'store/sproduct2.html', context)
def sp3(request):
      context = {}
      return render(request, 'store/sproduct3.html', context)
def sp4(request):
      context = {}
      return render(request, 'store/sproduct4.html', context)
def sp5(request):
      context = {}
      return render(request, 'store/sproduct5.html', context)
def sp6(request):
      context = {}
      return render(request, 'store/sproduct6.html', context)
def sp7(request):
      context = {}
      return render(request, 'store/sproduct7.html', context)
def sp8(request):
      context = {}
      return render(request, 'store/sproduct8.html', context)
def sp9(request):
      context = {}
      return render(request, 'store/sproduct9.html', context)
def sp10(request):
      context = {}
      return render(request, 'store/sproduct10.html', context)
def sp11(request):
      context = {}
      return render(request, 'store/sproduct11.html', context)
def sp12(request):
      context = {}
      return render(request, 'store/sproduct12.html', context)
def sp13(request):
      context = {}
      return render(request, 'store/sproduct13.html', context)
def sp14(request):
      context = {}
      return render(request, 'store/sproduct14.html', context)
def main(request):
      context = {}
      return render(request, 'store/index.html', context)
@csrf_exempt
def updateItem(request):

    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print("Action:", action)
    print("Products:", productId)  

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer , complete=False)
    orderitem, created = OrderItem.objects.get_or_create(order= order,product=product)

    if action == 'add':
        orderitem.quantity = (orderitem.quantity +1)  
    elif action == 'remove':
        orderitem.quantity = (orderitem.quantity -1)    
    orderitem.save()
    
    if orderitem.quantity <= 0:
        orderitem.delete()
    return JsonResponse("Item was added", safe=False)


