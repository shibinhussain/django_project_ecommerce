from django.shortcuts import render,redirect
from app1.models import login_tb,createaccount, product_details, seller_details, order_details
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage


# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def admin(request):
    return render(request,'admin1.html')


def go(request):
    if request.method=="POST":
        data=login_tb.objects.all()
        username=request.POST.get("username")
        password=request.POST.get("password")
        flag=0
        for d in data:
            if d.username==username and d.password==password:
                category1=d.category
                flag=1
                request.session["username"]=username
                if category1=="admin":
                    return redirect("/admin1")
                elif category1=="customer":
                    return redirect("/custhome")
                else:
                    return HttpResponse("invalid")   
        if flag==0:
            return HttpResponse("user does not exist")           
def signup(request):
    return render(request,"create_account.html")
def custhome(request):
    return render(request,'customer.html')

def custCreate(request):
    if request.method=='POST':
        var = createaccount()
        var.name =request.POST.get('name')
        var.email =request.POST.get('email')
        var.phone =request.POST.get('phone')
        var.address =request.POST.get('address')
        var.save()

        tb = login_tb()
        tb.username = request.POST.get('email')
        tb.password = request.POST.get('phone')
        tb.category ="customer"
        tb.save()

        return render (request,"login.html")


def pdt_detail(request):
    return render(request, "pdt-detail.html")

def pdt_insert(request):
    if request.method=='POST':
        ob = product_details()
        ob.productname=request.POST.get("pdt-name")
        ob.quantity=request.POST.get("qty")
        ob.price=request.POST.get("price")
        ob.offer=request.POST.get("ofr")
        # image
        item = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(item.name,item)
        up_file_url = fs.url(filename)
        ob.item=up_file_url
    
        ob.save()
        return redirect("/pdt-detail")

def pdt_view(request):
    obj = product_details.objects.all()
    return render(request, "pdt-view.html", {'ob': obj})

def pdt_edit(request, id):
    obj = product_details.objects.get(id=id)
    return render(request, "pdt-edit.html", {'ob': obj})

def pdt_update(request, id):
    if request.method=='POST':
        ob = product_details.objects.get(id=id)
        ob.productname=request.POST.get("pdt-name")
        ob.quantity=request.POST.get("qty")
        ob.price=request.POST.get("price")
        ob.offer=request.POST.get("ofr")
        ob.item=request.POST.get("image")
        ob.save()
        return redirect("/pdt-view")

def delete(request, id):
    obj = product_details.objects.get(id=id)
    obj.delete()
    return redirect("/pdt-view")
def complaint(request):
    return render(request,"complaints.html")

def seller(request):
    return render(request,"sellerdetails.html")

def sel_insert(request):
    if request.method=='POST':
        ob = seller_details()
        ob.sellerid = request.POST.get("sel_id")
        ob.sellername = request.POST.get("sel_name")
        ob.age = request.POST.get("age")
        ob.exp = request.POST.get("exp")
        ob.sal = request.POST.get("sal")
        ob.save()

        var =login_tb()
        var.username = request.POST.get("sel_name")
        var.password = request.POST.get("sel_id")
        var.category = "seller"
        var.save()

        return redirect("/seller_details")

def view_sel(request):
    obj = seller_details.objects.all()
    return render(request, "view-sel.html", {'ob': obj})


def sel_edit(request, id):
    obj = seller_details.objects.get(id=id)
    return render(request, "sell-edit.html", {'ob': obj})


def sel_delete(request, id):
    obj = seller_details.objects.get(id=id)
    obj.delete()
    return redirect("/view-seller")

def sell_update(request, id):
    if request.method=='POST':
        ob = seller_details.objects.get(id=id)
        ob.sellerid=request.POST.get("sel_id")
        ob.sellername=request.POST.get("sel_name")
        ob.age=request.POST.get("age")
        ob.exp=request.POST.get("exp")
        ob.sal=request.POST.get("sal")
        ob.save()
        return redirect("/view-seller")

# customer
def cusProduct(request):
    obj = product_details.objects.all()
    return render(request, "cus-productdetails.html", {'ob': obj})
def cusOrderPdts(request, id):
    obj = product_details.objects.get(id=id)
    return render(request, "order_details.html", {'ob': obj})


def orderPdtSub(request):
    if request.method=='POST':
        ob = order_details()
        ob.name=request.POST.get("name")
        ob.address=request.POST.get("address")
        ob.phone=request.POST.get("phone")
        ob.productname=request.POST.get("pdtname")
        ob.price=request.POST.get("price")
        ob.save()
        return redirect("/cusproduct")  

def review(request):
    obj = product_details.objects.all()
    return render(request, "review.html", {'ob': obj})

def add_review(request):
    return render(request, "add-review.html")


