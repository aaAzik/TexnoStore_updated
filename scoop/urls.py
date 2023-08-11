from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('create', views.sale_create, name="create"),
    path('collections', views.collections, name="collections"),
    path('collections/<pk>/delete/', views.sale_delete, name="sale_delete"),
    path('collections/<pk>/update/', views.sale_update, name="sale_update"),
    path('collections/<str:slug>', views.collectionsview, name="collectionsview"),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productview, name="productview")
]