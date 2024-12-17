
from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from t4app.models import Product
from django.db.models import Q 
import random
# Create your views here.



def product(request):
    p=Product.objects.all    #print(p)
    context={}
    context['data']=p 
    return render(request,'index.html',context)

def delete(request,rid):
    m=Product.objects.filter(id=rid)
    #print(m)
    m.delete()
    return redirect('/product')


def product_details(request,pid):
    p=Product.objects.filter(id=pid)
    context={}
    context['data']=p
    return render(request,'product_details.html',context)

def add_product(request):
    if request.method=="GET":
        return render(request,'add_product.html')
    else:
        n=request.POST['pname']
        p=request.POST['price']
        cat=request.POST['pcat']
        pd=request.POST['pdetail']
        img=request.POST['pimg']
        print(img)

        m=Product.objects.create(name=n,price=p,cat=cat,pdetails=pd,pimage=img)
        m.save()
        return redirect('/product')


def search(request):
    context={}
    query=request.GET['query']
    #print(query)
    pname=Product.objects.filter(name__icontains=query)
    pdetail=Product.objects.filter(pdetails__icontains=query)
    pcat=Product.objects.filter(cat__icontains=query)
    allproducts=pname.union(pdetail,pcat)
    if allproducts.count()==0:
        context['errmsg']='Products Not Found'
    context['data']=allproducts
    return render(request,'index.html',context)