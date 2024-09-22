from django.shortcuts import render,redirect
from Admin.models import *
# Create your views here.
def Category(request):
    try:
        if 'aid' in request.session:
            category = tbl_category.objects.all()
            if request.method == "POST":
                tbl_category.objects.create(category_name=request.POST.get("Category"))
                return render(request,'Admin/Category.html',{"msg":"Data Inserted"})
            else:
                return render(request,'Admin/Category.html',{"category":category})
        else:
            return redirect("Guest:Login")
    except:
        return redirect("Admin:errorpage")
        
def deletecategory(request,did):
    try:
        tbl_category.objects.get(id=did).delete()
        return redirect("Admin:Category")
    except:
        return redirect("Admin:errorpage")

def editcategory(request,eid):
    try:
        category= tbl_category.objects.get(id=eid)
        if request.method == "POST":
            category.category_name = request.POST.get("Category")
            category.save()
            return redirect("Admin:Category")
        else:
            return render(request,"Admin/Category.html",{"editcategory":category})
    except:
        return redirect("Admin:errorpage")

def deletebrand(request,dd):
    try:
        tbl_brands.objects.get(id=dd).delete()
        return redirect("Admin:Brand")
    except:
        return redirect("Admin:errorpage")

def editbrand(request,ebid):
    try:
        brand=tbl_brands.objects.get(id=ebid)
        if request.method == "POST":
            brand.brand_name=request.POST.get("Brand")
            brand.save()
            return redirect("Admin:Brand")
        else:
            return render(request,"Admin/Brand.html",{"editbrand":brand})
    except:
        return redirect("Admin:errorpage")

def Brand(request):
    try:
        if 'aid' in request.session:
            brand = tbl_brands.objects.all()
            if request.method == "POST":
                tbl_brands.objects.create(brand_name=request.POST.get("Brand"))
                return render(request,'Admin/Brand.html',{"msg":"Data Inserted"})
            else:
                return render(request,'Admin/Brand.html',{"brand":brand})
        else:
            return redirect("Guest:Login")
    except:
        return redirect("Admin:errorpage")

def Admin_Registration(request):
    try:
        if 'aid' in request.session:
            registration = tbl_admregistration.objects.all()
            if request.method == "POST":
                tbl_admregistration.objects.create(admregistration_name=request.POST.get("Name"),
                                                admregistration_email=request.POST.get("Email"),
                                                admregistration_password=request.POST.get("password"))
                return render(request,'Admin/Admin_Registration.html',{"msg":"Data Inserted"})
            else:
                return render(request,'Admin/Admin_Registration.html',{"registration":registration})
        else:
            return redirect("Guest:Login")
    except:
        return redirect("Admin:errorpage")

def deleteregistration(request,dele):
    try:
        tbl_admregistration.objects.get(id=dele).delete()
        return redirect("Admin:Admin_Registration")
    except:
        return redirect("Admin:errorpage")

def Subcategory(request):
    try:
        if 'aid' in request.session:
            cat=tbl_category.objects.all()
            subcategory = tbl_subcategory.objects.all()
            if request.method == "POST":
                tbl_subcategory.objects.create(subcategory_name=request.POST.get("Subcategory"),
                                            category=tbl_category.objects.get(id=request.POST.get('sel_category'))
                                            )
                return render(request,'Admin/Subcategory.html',{"msg":"Data Inserted"})
            else:
                return render(request,'Admin/Subcategory.html',{"subcategory":subcategory,'category':cat})
        else:
            return redirect("Guest:Login")    
    except:
        return redirect("Admin:errorpage")

def deletesubcategory(request,dsid):
    try:
        tbl_subcategory.objects.get(id=dsid).delete()
        return redirect("Admin:Subcategory")
    except:
        return redirect("Admin:errorpage")
    
def editsubcategory(request,esid):
    try:
        cat=tbl_category.objects.all()
        subcategory=tbl_subcategory.objects.get(id=esid)
        if request.method == "POST":
            subcategory.subcategory_name=request.POST.get("Subcategory")
            subcategory.category=tbl_category.objects.get(id=request.POST.get('sel_category'))
            subcategory.save()
            return redirect("Admin:Subcategory")
        else:
            return render(request,"Admin/Subcategory.html",{"editsubcategory":subcategory,'category':cat})
    except:
        return redirect("Admin:errorpage")

def Shop(request):
    try:
        if 'aid' in request.session:
            shop=tbl_shop.objects.all()
            if request.method == "POST":
                tbl_shop.objects.create(shop_name=request.POST.get("Name"),
                                                shop_email=request.POST.get("txt_email"),
                                                shop_details=request.POST.get("Details"),
                                                shop_password=request.POST.get("Password"),
                                                shop_photo=request.FILES.get("filephoto"))

                return render(request,'Admin/Shop.html',{"msg":"Data Inserted"})
            else:
                return render(request,'Admin/Shop.html',{"shop":shop})
        else:
            return redirect("Guest:Login")
    except:
        return redirect("Admin:errorpage")

def deleteshop(request,dshid):
    try:
        tbl_shop.objects.get(id=dshid).delete()
        return redirect("Admin:Shop")
    except:
        return redirect("Admin:errorpage")

def editshop(request,eshid):
    try:
        shop=tbl_shop.objects.get(id=eshid)
        if request.method == "POST":
            shop.shop_name=request.POST.get("Name")
            shop.shop_email=request.POST.get("txt_email")
            shop.shop_details=request.POST.get("Details")
            shop.shop_password=request.POST.get("Password")
            shop.shop_photo=request.FILES.get("filephoto")
            shop.save()
            return redirect("Admin:Shop")
        else:
            return render(request,"Admin/Shop.html",{"editshop":shop})
    except:
        return redirect("Admin:errorpage")
    
def Product(request):
    try:
        if 'aid' in request.session:
            cat=tbl_category.objects.all()
            brands=tbl_brands.objects.all()
            products=tbl_product.objects.all()
            if request.method == "POST":
                tbl_product.objects.create(product_name=request.POST.get("Name"),
                                            product_details=request.POST.get("Details"),
                                            product_price=request.POST.get("Price"),
                                            product_photo=request.FILES.get("productphoto"),
                                            brand=tbl_brands.objects.get(id=request.POST.get("selbrand")),
                                            subcategory=tbl_subcategory.objects.get(id=request.POST.get("sel_subcategory")))
                return render(request,'Admin/Product.html',{"msg":"Data Inserted"})
            else:
                return render(request,'Admin/Product.html',{'category':cat,'brands':brands,'products':products})
        else:
            return redirect("Guest:Login")
    except:
        return redirect("Admin:errorpage")

def ajaxsubcategory(request):
    try:
        cat = tbl_category.objects.get(id=request.GET.get("did"))
        Subcategory = tbl_subcategory.objects.filter(category=cat)
        return render(request,"Admin/AjaxSubcategory.html",{"subcategory":Subcategory})
    except:
        return redirect("Admin:errorpage")

def deleteproduct(request,dpid):
    try:
        tbl_product.objects.get(id=dpid).delete()
        return redirect("Admin:Product")
    except:
        return redirect("Admin:errorpage")

def homepage(request):
    try:
        if 'aid' in request.session:
            admin = tbl_admregistration.objects.get(id=request.session["aid"])
            return render(request,'Admin/Homepage.html',{"admin":admin})
        else:
            return redirect("Guest:Login")
    except:
        return redirect("Admin:errorpage")
    
def errorpage(request):
    return render(request,'Admin/Error.html')

def logout(request):
    try:
        del request.session["aid"]
        return redirect("Guest:Login")
    except:
        return redirect("Admin:errorpage")