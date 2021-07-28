from django.shortcuts import render
from django.contrib import messages
from django.core import paginator
from django.http import HttpResponse
from .models import *
from product.models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def index(request):
    profile = Profile.objects.get(pk=1)
    manufacturers = Manufacturers.objects.all()
    category = Category.objects.all()[:9]
    category_a = Category.objects.all()[:4]
    new_prod= Product.objects.filter(new_prod=True)[:6]
    carousel_a=Carousel_a.objects.get(pk=1)
    carousel_b=Carousel_b.objects.get(pk=1)
    carousel_c=Carousel_c.objects.get(pk=1)
    carousel_d=Carousel_d.objects.get(pk=1)
    featured=Product.objects.filter(featured=True)

    context = {
        'profile': profile,
        'manufacturers': manufacturers,
        'category': category,
        'category_a': category_a,
        'new_prod': new_prod,
        'carousel_a': carousel_a,
        'carousel_b': carousel_b,
        'carousel_c': carousel_c,
        'carousel_d': carousel_d,
        'featured': featured,
    }


    
    return render(request, 'index.html', context)


def category(request):
    profile=Profile.objects.get(pk=1)
    manufacturers= Manufacturers.objects.all()
    category = Category.objects.order_by('-created_at').filter(status=True)
    category_a = Category.objects.all()[:4]
    paginator = Paginator(category, 8)
    page = request.GET.get('page')
    paged_category = paginator.get_page(page)

    context = {
        'profile': profile,
        'manufacturers': manufacturers,
        'category': paged_category,
        'category_a': category_a,
    }


    return render(request, 'category.html', context)


def prod_list(request,id,slug):
    profile=Profile.objects.get(pk=1)
    category=Category.objects.all()
    category_a = Category.objects.all()[:4]
    product=Product.objects.filter(category_id=id)
    products=Product.objects.get(pk=id)
    manufacturers=Manufacturers.objects.all()

    context = {
        'profile': profile,
        'category': category,
        'product': product,
        'products': products,
        'manufacturers': manufacturers,
        'category_a': category_a,
    }

    return render(request, 'prod-list.html', context)

def prod_detail(request,id,slug):
    profile=Profile.objects.get(pk=1)
    category=Category.objects.all()
    category_a = Category.objects.all()[:4]
    product=Product.objects.filter(category_id=id)
    products=Product.objects.get(pk=id)
    manufacturers=Manufacturers.objects.all()
    images = Images.objects.filter(product_id=id)

    context = {
        'profile': profile,
        'category': category,
        'product': product,
        'products': products,
        'manufacturers': manufacturers,
        'category_a': category_a,
        'images': images,
    }
    return render(request, 'prod-details.html', context)