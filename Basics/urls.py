from django.urls import path
from Basics import views
urlpatterns=[
    path('sum/',views.sum,name='sum'),
    path('sumofThree/',views.sumofThree,name='sumofThree')
]