
from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from t4app.models import Product
from django.db.models import Q 
import random
# Create your views here.



def product(request):
    uid=request.user.id
    #print('logging user',uid)
    p=Product.objects.filter(is_active=True)
    #print(p)
    context={}
    context['data']=p 
    return render(request,'index.html',context)




def product_details(request,pid):
    p=Product.objects.filter(id=pid)
    context={}
    context['data']=p
    return render(request,'product_details.html',context)




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