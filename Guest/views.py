from django.shortcuts import render,redirect
from Admin.models import *
# Create your views here.
def Login(request):
    try:
        if request.method=="POST":
            email=request.POST.get('txtemail')
            password=request.POST.get('txtpassword')
            admin=tbl_admregistration.objects.filter(admregistration_email=email,admregistration_password=password).count()
            shop=tbl_shop.objects.filter(shop_email=email,shop_password=password).count()
            if(admin > 0):
                admin=tbl_admregistration.objects.get(admregistration_email=email,admregistration_password=password)
                request.session['aid']=admin.id
                return redirect('Admin:homepage')
            elif(shop > 0):
                shop=tbl_shop.objects.get(shop_email=email,shop_password=password)
                request.session['sid']=shop.id
                return redirect('ShopManager:shophomepage')
            else:
                return render(request,'Guest/Login.html')
        else:
            return render(request,'Guest/Login.html')
    except:
        return redirect("Guest:errorpage")

def errorpage(request):
    return render(request,'Guest/Error.html')

def index(request):
    return render(request,'Guest/index.html')