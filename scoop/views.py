from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "scoop/main.html")

def contact(request):
    return render(request, "scoop/contact.html")

def collections(request):
    print(request.user.username)
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

@login_required(redirect_field_name='login')    
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



@login_required(redirect_field_name='login')
def sale_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            Product.objects.create(
                category = cd['category'],
                name = cd['name'],
                product_image = cd['product_image'],
                description = cd['description'],
                price = cd['price'],
                )
            return redirect(to='collections')
    else:
        form = ProductForm()
    context = {
        'form':form
    }
    return render(request, "scoop/create.html", context)


def sale_delete(request, pk):
    products = Product.objects.get(id=pk)
    products.delete()
    return redirect(to='collections')

def sale_update(request, pk):
    products = Product.objects.get(id=pk)
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.cleaned_data['category']
            slug = form.cleaned_data['slug']
            name = form.cleaned_data['name']
            product_image = form.cleaned_data['product_image']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            author = form.cleaned_data['author']
            products.category = category
            products.slug = slug
            products.name = name
            products.product_image = product_image
            products.description = description
            products.price = price
            products.author = author
            products.save()
            return redirect(to='collections')
    else:
        form = ProductForm()
    context = {
        'form':form
    }
    return render(request, "scoop/update.html",context)
