from django.shortcuts import render, redirect
from store.forms import*
from store.models import*

def Home(request):
    return render(request,'home.html')

def Contact(request):
    return render(request,'contact.html')



def Addproduct(request):
    if request.method =="POST":
        form = productform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addproduct')
    else:
        form =productform(request.FILES)
    return render(request,"product.html",{'form':form})


def showdata(request):  
    a = Product.objects.all()  
    return render(request,"view.html",{'user':a}) 
   

def Deletedata(request,id):
   b = Product.objects.get(id=id)
   b.delete()
   return redirect("showdata")


def Update(request,id):
    c = Product.objects.get(id=id)
    update =productform(request.POST or None,request.FILES or None, instance=c)
    if update.is_valid():
        update.save()
        return redirect('showdata')
    return render(request,"update.html",{"update":update})
    
