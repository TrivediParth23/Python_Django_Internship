from django.shortcuts import render
from django.http import HttpResponse
from .models import product ,contact,order
from math import ceil

def index(request):
    allprod = []
    catprods = product.objects.values('category','id')
    cats = {item['category']for item in catprods}
    for cat in cats:
        prod=product.objects.filter(category=cat)
        n = len(prod)
        nslide = n // 4 + ceil((n / 4) - (n // 4))
        allprod.append([prod,range(1,nslide), nslide])
    params={'allprods':allprod}
    return render(request,'shop/index.html',params)

def SearchMatch(query,item):
    if query in item.decs.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:    
        return False

def search(request):
    query = request.GET.get('search')
    allprod = []
    catprods = product.objects.values('category','id')
    cats = {item['category']for item in catprods}
    for cat in cats:
        prodtemp = product.objects.filter(category=cat)
        prod = [item for item in prodtemp if SearchMatch(query,item)]
        n = len(prod)   
        nslide = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allprod.append([prod,range(1,nslide), nslide])
    params={'allprods':allprod,"msg":""}
    if len(allprod) == 0 or len(query)<3:
        params = {"msg":"Please Enter Valid Product Description.."}
    return render(request,'shop/search.html',params)

def about(request):
    return render(request,'shop/about.html')

def productview(request, myid):
    products = product.objects.filter(id=myid)
    print(products)
    return render(request,'shop/prodview.html',{'products':products[0]})

def checkout(request):
    if request.method=="POST":
        item_json = request.POST.get('itemsJson','')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        mobile_number = request.POST.get('mobile_number', '')
        tick_marked = request.POST.get('tick_marked', '')
        print(name, email, address, city, state,zip_code,mobile_number)
        orderdata = order(item_json=item_json,name=name, email=email, address=address, city=city, state=state,zip_code=zip_code,mobile_number=mobile_number,tick_marked=tick_marked)
        orderdata.save()
        thank = True
        return render(request, 'shop/checkout.html', {'thank':thank})
    return render(request, 'shop/checkout.html')


def ourvision(request):
    return render(request,'shop/Our Vision.html')

def ourcompany(request):
    return render(request,'shop/Our Company.html')

def contactus(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email-id','')
        address1 = request.POST.get('address1','')
        address2 = request.POST.get('address2','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        query = request.POST.get('query','')
        tick = request.POST.get('tick','')
        print(name, email, address1, address2, city, state, query, tick)
        contactdata = contact(name=name, email=email, address1=address1, address2=address2, city=city, state=state,query=query,tick=tick)
        contactdata.save()
        thank = True
        return render(request, 'shop/Contact Us.html', {'thank': thank})
    return render(request,'shop/Contact Us.html')

def myorders(request):
    return render(request,'shop/Myorders.html')

def mycart(request):
    return render(request,'shop/Mycart.html')






