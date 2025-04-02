from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name='index'),
    path("about/",views.about, name='about'),
    path("our vision/",views.ourvision, name='ourVision'),
    path("our company/",views.ourcompany, name='ourCompany'),
    path("search/",views.search, name='Search'),
    path("products/<int:myid>/",views.productview, name='productview'),
    path("checkout/",views.checkout, name='checkout'),
    path("contact us/",views.contactus, name='contact Us'),
    path("myorders/",views.myorders, name='myOrders'),
    path("mycart/",views.mycart, name='myCart')
]