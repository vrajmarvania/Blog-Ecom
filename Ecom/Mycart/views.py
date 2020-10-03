import json
from math import ceil

import order as order
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product,Contect,Order,Orderupdate

def ind(request):


     # n = len(products)
     # nSlides = n // 4 + ceil((n / 4) - (n // 4))
     # allProds = [[products, range(1, len(products)), nSlides], [products, range(1, len(products)), nSlides]]

     products = Product.objects.all()
     allpro=[]
     catpro= Product.objects.values('category')
     cats={item["category"] for item in catpro}
     for cat in cats:
          prod=Product.objects.filter(category=cat)
          n=len(prod)
          nSlides = n // 4 + ceil((n / 4) - (n // 4))
          allpro.append([prod, range(1, nSlides), nSlides])

     params = {'allProds': allpro }
     return render(request, "Mycart/index.html", params)

def about(request):
     return render(request, 'Mycart/about.html')
def contact(request):
    if request.method == "POST":
      Name=request.POST.get('name','')
      Email=request.POST.get('Email','')
      Phone=request.POST.get('phone','')
      N_help=request.POSTp.get('desc','')
      contact=Contect(Name=Name,Email=Email,Phone=Phone,N_help=N_help)
      contact.save()
    return render(request, 'Mycart/contact.html')

# def tracker(request):
#     if request.method=="POST":
#       id=request.POST.get('id','')
#       Email = request.POST.get('Email', '')
#       try:
#        order=Order.objects.filter(id="id",Email="Email")
#        if(order>0):
#            update=Orderupdate.objects.filter(order)
#
#
#        except:
#              print("hello")
#
#      return render(request, 'Mycart/tracker.html')

def tracker(request):

        id = request.POST.get('id', '')
        Email = request.POST.get('Email', '')

        try:
            order = Order.objects.filter(id=id, Email=Email)
            if len(order)>0:
                update = Orderupdate.objects.filter(id=id)
                print(update)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)

                return HttpResponse(response)
            else:

                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse({})

    return render(request, 'Mycart/tracker.html')


def search(request):
     return render(request, 'Mycart/search.html')

def productview(request, myid):
     product=Product.objects.filter(id=myid)

     return render(request, 'Mycart/productview.html',{'product':product[0]})

def checkout(request):
     return render(request, 'Mycart/checkout.html')

def order(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')


        Name=request.POST.get('Name','')
        Email = request.POST.get('Email', '')
        Address = request.POST.get('Address', '')
        City = request.POST.get('City', '')
        State = request.POST.get('State', '')
        Zip = request.POST.get('Zip', '')
        Phone = request.POST.get('Phone', '')
        order=Order(items_json=items_json,Name=Name,Email=Email,Address=Address,City=City,State=State,Zip=Zip,Phone=Phone)
        order.save()
        ord=Orderupdate(id=order.id,update_desc="Your order has been placed..")
        ord.save()
        thank = True
        id = Order.id
        return render(request, 'Mycart/checkout.html', {'thank': thank, 'id': id})
    return render(request,'Mycart/checkout.html')


