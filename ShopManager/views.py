from django.shortcuts import render,redirect
from Admin.models import*
from ShopManager.models import*
from django.http import JsonResponse
from django.db.models import Sum
import random
from datetime import date
# Create your views here.

def shophomepage(request):
    try:
        if 'sid' in request.session:
            shop = tbl_shop.objects.get(id=request.session["sid"])
            return render(request,'ShopManager/HomePage.html',{"shop":shop})
        else:
            return redirect("Guest:Login")
    except:
        return redirect("ShopManager:errorpage")

def errorpage(request):
    return render(request,'ShopManager/Error.html')

def viewproduct(request):
    try:
        if 'sid' in request.session:
            products = tbl_product.objects.all()
            return render(request,'ShopManager/ViewProduct.html',{'products':products})
        else:
            return redirect("Guest:Login")
    except:
        return redirect("ShopManager:errorpage")

def ajaxsearchproduct(request):
    try:
        products = tbl_product.objects.filter(product_name__istartswith=request.GET.get("num"))
        return render(request,'ShopManager/AjaxSearchProduct.html',{'products':products})
    except:
        return redirect("ShopManager:errorpage")

def stock(request,id):
    try:
        stocks=tbl_stock.objects.filter(product_id=id,shop_id=request.session["sid"])
        if request.method == "POST":
            tbl_stock.objects.create(
                                    vendor_name=request.POST.get("Vendor name"),
                                    stock_quantity=request.POST.get("Stock quantity"),
                                    product_id=tbl_product.objects.get(id=id),
                                    shop_id=tbl_shop.objects.get(id=request.session['sid']))
            return render(request,'ShopManager/Stock.html',{"msg":"Data inserted"})
        else:
                
            return render(request,'ShopManager/Stock.html',{'stocks':stocks,"productid":id})
    except:
        return redirect("ShopManager:errorpage")

def deletestock(request,dsid,pdtid):
    try:
        tbl_stock.objects.get(id=dsid).delete()
        return redirect("ShopManager:stock",pdtid)
    except:
        return redirect("ShopManager:errorpage")

def customer(request):
    try:
        if 'sid' in request.session:
            customers=tbl_customer.objects.all()
            if request.method == "POST":
                tbl_customer.objects.create(customer_name=request.POST.get("Name"),
                                                customer_contact=request.POST.get("Contact"),
                                                )
                return render(request,'ShopManager/Customer.html',{"msg":"Data inserted"})
            else:
                return render(request,'ShopManager/Customer.html',{"customers":customers})
        else:
            return redirect("Guest:Login")
    except:
        return redirect("ShopManager:errorpage")

def deletecustomer(request,dcid):
    try:
        tbl_customer.objects.get(id=dcid).delete()
        return redirect("ShopManager:customer")
    except:
        return redirect("ShopManager:errorpage")

def viewcustomer(request):
    try:
        customers=tbl_customer.objects.all()
        return render (request,'ShopManager/ViewCustomer.html',{'customers':customers})
    except:
        return redirect("ShopManager:errorpage")

def searchcustomer(request):
    try:
        if 'sid' in request.session:
            if request.method == "POST":
                customercount= tbl_customer.objects.filter(customer_contact=request.POST.get("Number")).count()
                if customercount > 0:
                    customer = tbl_customer.objects.get(customer_contact=request.POST.get("Number"))
                    return redirect("ShopManager:shopproduct",customer.id)
                else:
                    customer = tbl_customer.objects.create(customer_contact=request.POST.get("Number"),customer_name=request.POST.get("Name"))
                    return redirect("ShopManager:shopproduct",customer.id)
            else:
                return render(request,'ShopManager/SearchCustomer.html')
        else:
            return redirect("Guest:Login")
    except:
        return redirect("ShopManager:errorpage")

def ajaxcustomer(request):
    try:
        customercount= tbl_customer.objects.filter(customer_contact=request.GET.get("num")).count()
        if customercount > 0:
            customer = tbl_customer.objects.get(customer_contact=request.GET.get("num"))
            return JsonResponse({"msg":customer.customer_name})
        else:
            return JsonResponse({"msg":"No User Found"})
    except:
        return redirect("ShopManager:errorpage")    
    
def shopproduct(request,id):
    try:
        if request.method == "POST":
            purchasecount = tbl_purchase.objects.filter(customer=id,purchase_status=0).count()
            if purchasecount > 0:
                return redirect("ShopManager:viewlist",id)
            else:
                return render(request,"ShopManager/ShopProduct.html",{"msg":"Please Select Any Item","customer":id})
        else:
            stock = tbl_stock.objects.filter(shop_id=request.session["sid"])
            # print(stock)
            pdtid = {}
            pdtids = []
            listappent = []
            for i in stock:
                listappent.append(i.product_id.id)
            pdtid = set(listappent)
            # print(pdtid)
            pdtids = list(pdtid)
            # print(pdtids)
            products =tbl_product.objects.filter(id__in=pdtids)
            # print(products)
            for i in products:
                stock = tbl_stock.objects.filter(product_id=i.id,shop_id=request.session["sid"]).aggregate(total=Sum('stock_quantity'))['total']
                cart = tbl_items.objects.filter(product=i.id,purchase__purchase_status=1,purchase__shop=request.session["sid"]).aggregate(total=Sum('item_qty'))['total']
                # print(cart)
                if stock is None:
                    stock = 0
                if cart is None:
                    cart = 0
                total = stock - cart
                i.stocktotal = total
            return render(request,"ShopManager/ShopProduct.html",{"products":products,"customer":id})
    except:
        return redirect("ShopManager:errorpage")
   
def ajaxsearchitem(request):
    try:
        stock = tbl_stock.objects.filter(shop_id=request.session["sid"])
        # print(stock)
        pdtid = {}
        pdtids = []
        listappent = []
        for i in stock:
            listappent.append(i.product_id.id)
        pdtid = set(listappent)
        # print(pdtid)
        pdtids = list(pdtid)
        products =tbl_product.objects.filter(id__in=pdtids,product_name__istartswith=request.GET.get("num"))
        for i in products:
            stock = tbl_stock.objects.filter(product_id=i.id,shop_id=request.session["sid"]).aggregate(total=Sum('stock_quantity'))['total']
            cart = tbl_items.objects.filter(product=i.id,purchase__purchase_status=1,purchase__shop=request.session["sid"]).aggregate(total=Sum('item_qty'))['total']
            # print(cart)
            if stock is None:
                stock = 0
            if cart is None:
                cart = 0
            total = stock - cart
            i.stocktotal = total
        return render(request,"ShopManager/AjaxSearchItems.html",{"item":products})
    except:
        return redirect("ShopManager:errorpage")

def ajaxaddtocart(request):
    try:
        purchasecount = tbl_purchase.objects.filter(customer=request.GET.get("customer"),purchase_status=0).count()
        if purchasecount > 0:
            purchase = tbl_purchase.objects.get(customer=request.GET.get("customer"),purchase_status=0)
            itemcount = tbl_items.objects.filter(product=request.GET.get("product"), purchase=purchase).count()
            if itemcount > 0:
                return JsonResponse({"msg":"Already Added"})
            else:
                pdt = tbl_product.objects.get(id=request.GET.get("product"))
                tbl_items.objects.create(item_qty=1,item_price=pdt.product_price,product=tbl_product.objects.get(id=request.GET.get("product")),purchase=tbl_purchase.objects.get(id=purchase.id))
                return JsonResponse({"msg":"Item Added"})
        else:
            purchase = tbl_purchase.objects.create(customer=tbl_customer.objects.get(id=request.GET.get("customer")),shop=tbl_shop.objects.get(id=request.session["sid"]))
            pdt = tbl_product.objects.get(id=request.GET.get("product"))
            tbl_items.objects.create(item_qty=1,item_price=pdt.product_price,product=tbl_product.objects.get(id=request.GET.get("product")),purchase=tbl_purchase.objects.get(id=purchase.id))
            return JsonResponse({"msg":"Item Added"})
    except:
        return redirect("ShopManager:errorpage")
    
def billing(request):
    try:
        shop = tbl_shop.objects.get(id=request.session["sid"])
        purchasecount=tbl_purchase.objects.filter(purchase_status=0).count()
        if purchasecount >0:
            purchase=tbl_purchase.objects.get(purchase_status=0)
            request.session['pid']=purchase.id
            item=tbl_items.objects.filter(purchase=purchase)
            for i in item:
                pdt=i.product.id
                stk=tbl_stock.objects.filter(shop_id=request.session['sid'],product_id=pdt)
            for i in stk:
                stock= i.stock_quantity
        return render(request,'ShopManager/Billing.html',{'items':item,'stock':stock,"shop":shop})
    except:
        return redirect("ShopManager:errorpage")

def Qty(request):
    try:
        qty=request.GET.get('QTY')
        itemid=request.GET.get('ALT')
        itemdata=tbl_items.objects.get(id=itemid)
        itemdata.item_qty=qty
        
        itemdata.save()
        return redirect("ShopManager:billing") 
    except:
        return redirect("ShopManager:errorpage")

def viewlist(request,id):
    try:
        if request.method == "POST":
            purchase = tbl_purchase.objects.get(customer=id,purchase_status=0)
            purchase.purchase_status = 1
            purchase.save()
            return redirect("ShopManager:bill",purchase.id)
        else:
            items  = tbl_items.objects.filter(purchase__customer=id,purchase__purchase_status=0)
            grandtotal = 0
            for i in items:
                grandtotal = grandtotal + (int(i.item_qty) * int(i.product.product_price))

                stock = tbl_stock.objects.filter(product_id=i.product.id,shop_id=request.session["sid"]).aggregate(total=Sum('stock_quantity'))['total']
                cart = tbl_items.objects.filter(product=i.product.id,purchase__purchase_status=1,purchase__shop=request.session["sid"]).aggregate(total=Sum('item_qty'))['total']
                # print(cart)
                if stock is None:
                    stock = 0
                if cart is None:
                    cart = 0
                total = stock - cart
                i.stocktotal = total
            return render(request,'ShopManager/View_List.html',{"items":items,"customer":id, "total":grandtotal})
    except:
        return redirect("ShopManager:errorpage")

def ajaxdeleteitem(request):
    try:
        item = tbl_items.objects.get(id=request.GET.get("itemid"))
        itemcount = tbl_items.objects.filter(purchase=item.purchase.id).count()
        if itemcount > 1:
            tbl_items.objects.get(id=request.GET.get("itemid")).delete()
            return JsonResponse({"msg":"Item Deleted","status":0})
        else:
            tbl_items.objects.get(id=request.GET.get("itemid")).delete()
            tbl_purchase.objects.get(id=item.purchase.id).delete()
            return JsonResponse({"msg":"Purchase Cancelled","status":1})
    except:
        return redirect("ShopManager:errorpage")

def ajaxitemqtyupdate(request):
    try:
        item = tbl_items.objects.get(id=request.GET.get("itemid"))
        product = tbl_product.objects.get(id=item.product.id)
        productprice = product.product_price
        total = int(productprice) * int(request.GET.get("quantity"))
        item.item_qty = request.GET.get("quantity")
        item.item_price = total
        item.save()
        return JsonResponse({"msg":"Quantity Updated"})
    except:
        return redirect("ShopManager:errorpage")

def bill(request, id):
    try:
        shop = tbl_shop.objects.get(id=request.session["sid"])
        invoice_number = random.randint(000000,999999)
        purchase = tbl_purchase.objects.get(id=id)
        customer = purchase.customer.id
        grandtotal = 0
        items = tbl_items.objects.filter(purchase=id)
        for i in items:
                grandtotal = grandtotal + (int(i.item_qty) * int(i.product.product_price))
        return render(request,"ShopManager/Bill.html",{"inumber":invoice_number,"purchase":purchase,"total":grandtotal,"item":items,"shop":shop,"customer":customer})
    except:
        return redirect("ShopManager:errorpage")

def logout(request):
    try:
        del request.session["sid"]
        return redirect("Guest:Login")
    except:
        return redirect("ShopManager:errorpage")
    
def viewstock(request):
    try:
        if 'sid' in request.session:
            stock = tbl_stock.objects.filter(shop_id=request.session["sid"])
            # print(stock)
            pdtid = {}
            pdtids = []
            listappent = []
            for i in stock:
                listappent.append(i.product_id.id)
            pdtid = set(listappent)
            # print(pdtid)
            pdtids = list(pdtid)
            # print(pdtids)
            products =tbl_product.objects.filter(id__in=pdtids)
            # print(products)
            for i in products:
                stock = tbl_stock.objects.filter(product_id=i.id,shop_id=request.session["sid"]).aggregate(total=Sum('stock_quantity'))['total']
                cart = tbl_items.objects.filter(product=i.id,purchase__purchase_status=1,purchase__shop=request.session["sid"]).aggregate(total=Sum('item_qty'))['total']
                # print(cart)
                if stock is None:
                    stock = 0
                if cart is None:
                    cart = 0
                total = stock - cart
                i.stocktotal = total
            return render(request,"ShopManager/View_stock.html",{"product":products})
        else:
            return redirect("Guest:Login")
    except:
        return redirect("ShopManager:errorpage")

def ajaxsearchstock(request):
    try:
        stock = tbl_stock.objects.filter(shop_id=request.session["sid"])
        # print(stock)
        pdtid = {}
        pdtids = []
        listappent = []
        for i in stock:
            listappent.append(i.product_id.id)
        pdtid = set(listappent)
        # print(pdtid)
        pdtids = list(pdtid)
        # print(pdtids)
        products =tbl_product.objects.filter(id__in=pdtids,product_name__istartswith=request.GET.get("num"))
        # print(products)
        for i in products:
            stock = tbl_stock.objects.filter(product_id=i.id,shop_id=request.session["sid"]).aggregate(total=Sum('stock_quantity'))['total']
            cart = tbl_items.objects.filter(product=i.id,purchase__purchase_status=1,purchase__shop=request.session["sid"]).aggregate(total=Sum('item_qty'))['total']
            # print(cart)
            if stock is None:
                stock = 0
            if cart is None:
                cart = 0
            total = stock - cart
            i.stocktotal = total
        return render(request,"ShopManager/AjaxViewstock.html",{"product":products})
    except:
        return redirect("ShopManager:errorpage")
    
def saleshistory(request):
    try:
        sales = tbl_items.objects.filter(purchase__shop=request.session["sid"])
        return render(request,"ShopManager/Sales_History.html",{"sales":sales})
    except:
        return redirect("ShopManager:errorpage")

def ajaxsearchsalehistory(request):
    try:
        sales = tbl_items.objects.filter(purchase__shop=request.session["sid"],product__product_name__istartswith=request.GET.get("num"))
        return render(request,"ShopManager/AjaxSalesHistory.html",{"sales":sales})  
    except:
        return redirect("ShopManager:errorpage")

def customerpurchaselist(request, id):
    try:
        purchase = tbl_purchase.objects.filter(customer=id,purchase_date__lt=date.today())
        for p in purchase:
            feed = tbl_feedback.objects.filter(customer=p.customer.id,purchase=p.id).count()
            if feed > 0:
                p.feedback = 1
            else:
                p.feedback = 0
        return render(request,"ShopManager/Customer_Purchaselist.html",{"purchase":purchase})
    except:
        return redirect("ShopManager:errorpage")

def customerproduct(request, id):
    try:
        purchase = tbl_purchase.objects.get(id=id)
        customer = purchase.customer.id
        items = tbl_items.objects.filter(purchase=id)
        for i in items:
            feed = tbl_feedback.objects.filter(product=i.product.id,customer=customer,purchase=purchase).count()
            if feed > 0:
                i.feedback = 1
            else:
                i.feedback = 0
        return render(request,'ShopManager/Customer_Product.html',{'item':items,"customer":customer,"purchase":id})
    except:
        return redirect("ShopManager:errorpage")

def givefeedback(request, id, customer, purchase):
    try:
        if request.method == "POST":
            tbl_feedback.objects.create(product=tbl_product.objects.get(id=id),quality=request.POST.get("sel_quality"),usability=request.POST.get("sel_usability"),price=request.POST.get("sel_price"),customer=tbl_customer.objects.get(id=customer),purchase=tbl_purchase.objects.get(id=purchase))
            return render(request,"ShopManager/GiveFeedback.html",{"msg":"Feedback Updated","purchase":purchase})
        else:
            return render(request, "ShopManager/GiveFeedback.html")
    except:
        return redirect("ShopManager:errorpage")