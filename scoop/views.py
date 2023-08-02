from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *

def home(request):
    return render(request, "scoop/main.html")

def contact(request):
    return render(request, "scoop/contact.html")

def collections(request):
    category = Category.objects.filter()
    context = {"category": category}
    return render(request, "scoop/insale.html",context)

def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug)):
        products = Product.objects.filter(category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first()
        context = {'products': products, 'category_name': category_name}
        return render(request, 'scoop/products/products.html', context)
    else:
        messages.warning(request, "No category")
        return redirect('collections')
    
def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug)):
        if(Product.objects.filter(slug=prod_slug)):
            products = Product.objects.filter(slug=prod_slug).first
            context = {'products': products}
        else:
            messages.error(request, "No product")
            return redirect('collections')
    else:
        messages.error(request, "No category")
        return redirect('collections')
    return render(request, "scoop/products/view.html", context)
