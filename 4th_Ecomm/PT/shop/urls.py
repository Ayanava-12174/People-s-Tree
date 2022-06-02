from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "ShopHome"),
    path("about/", views.about, name = "About"),
    path("contact/", views.contact, name = "Contacts"),
    path("tracker/", views.tracker, name = "TrackyourProduct"),
    path("search/", views.search, name = "Search"),
    path("products/<int:var_id>", views.productview, name = "Productview"),
    path("checkout/", views.checkout, name = "Checkout"),
    path("request_handler_payments/", views.request_handler_payments, name = "request_handler_payments"),
   
    
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)