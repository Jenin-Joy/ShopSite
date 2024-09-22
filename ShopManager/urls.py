from django.urls import path
from ShopManager import views
app_name="ShopManager"
urlpatterns=[
    path('shophomepage/',views.shophomepage,name='shophomepage'),
    
    path('viewproduct/',views.viewproduct,name='viewproduct'),
    path('ajaxsearchproduct/',views.ajaxsearchproduct,name='ajaxsearchproduct'),
    
    path('stock/<int:id>',views.stock,name='stock'),
    path('deletestock/<int:dsid>/<int:pdtid>',views.deletestock,name='deletestock'),
    path('customer/',views.customer,name='customer'),
    path('deletecustomer/<int:dcid>',views.deletecustomer,name='deletecustomer'),
    path('viewcustomer/',views.viewcustomer,name='viewcustomer'),
    path('searchcustomer/',views.searchcustomer,name='searchcustomer'),
    path('ajaxcustomer/',views.ajaxcustomer,name='ajaxcustomer'),
    path('shopproduct/<int:id>',views.shopproduct,name='shopproduct'),
    path('ajaxsearchitem/',views.ajaxsearchitem,name='ajaxsearchitem'),
    path('ajaxaddtocart/',views.ajaxaddtocart,name='ajaxaddtocart'),
    path('billing/',views.billing,name='billing'),
    path('Qty/',views.Qty,name='Qty'),

    path('viewlist/<int:id>',views.viewlist,name='viewlist'),
    path('ajaxdeleteitem/',views.ajaxdeleteitem,name='ajaxdeleteitem'),
    path('ajaxitemqtyupdate/',views.ajaxitemqtyupdate,name='ajaxitemqtyupdate'),
    path('bill/<int:id>',views.bill,name='bill'),

    path('logout/',views.logout,name='logout'),
    path('errorpage/',views.errorpage,name='errorpage'),

    path('viewstock/',views.viewstock,name='viewstock'),
    path('ajaxsearchstock/',views.ajaxsearchstock,name='ajaxsearchstock'),

    path('saleshistory/',views.saleshistory,name='saleshistory'),
    path('ajaxsearchsalehistory/',views.ajaxsearchsalehistory,name='ajaxsearchsalehistory'),


    path('customerpurchaselist/<int:id>',views.customerpurchaselist,name='customerpurchaselist'),
    path('customerproduct/<int:id>',views.customerproduct,name='customerproduct'),
    path('givefeedback/<int:id>/<int:customer>/<int:purchase>',views.givefeedback,name='givefeedback'),



]