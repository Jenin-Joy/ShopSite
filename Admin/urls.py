from django.urls import path
from Admin import views
app_name ="Admin"
urlpatterns=[
   path('Category/',views.Category,name='Category'),
   path('deletecategory/<int:did>',views.deletecategory,name="deletecategory"),
   path('editcategory/<int:eid>',views.editcategory,name="editcategory"),
   path('deletebrand/<int:dd>',views.deletebrand,name="deletebrand"),
   path('Brand/',views.Brand,name='Brand'),
   path('editbrand/<int:ebid>',views.editbrand,name="editbrand"),
   path('Admin_Registration/',views.Admin_Registration,name='Admin_Registration'),
   path('deleteregistration/<int:dele>',views.deleteregistration,name="deleteregistration"),
   path('Subcategory/',views.Subcategory,name='Subcategory'),
   path('deletesubcategory/<int:dsid>',views.deletesubcategory,name="deletesubcategory"),
   path('editsubcategory/<int:esid>',views.editsubcategory,name="editsubcategory"),
   path('Shop/',views.Shop,name='Shop'),
   path('deleteshop/<int:dshid>',views.deleteshop,name='deleteshop'),
   path('editshop/<int:eshid>',views.editshop,name="editshop"),
   path('Product/',views.Product,name='Product'),
   path('ajaxsubcategory/',views.ajaxsubcategory,name='ajaxsubcategory'),
   path('deleteproduct/<int:dpid>',views.deleteproduct,name="deleteproduct"),
   path('homepage/',views.homepage,name='homepage'),

   path('errorpage/',views.errorpage,name='errorpage'),
   path('logout/',views.logout,name='logout'),



]