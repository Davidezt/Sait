from django.shortcuts import render

from django.core.paginator import Paginator

from django.template.defaultfilters import register

from django.contrib.auth import authenticate

from services.products_module.models import Product


@register.filter()
def get_range(value):
    return range(1, value + 1)

def index(request):
    products = Product.objects.all()
    paginator = Paginator(products, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'products': page_obj,'pages_count': paginator.num_pages, 'page_number':page_number}
    return render(request, 'index.html',context)