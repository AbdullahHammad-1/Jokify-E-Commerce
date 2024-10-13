from django.shortcuts import render
from django.template.defaultfilters import title
from django.core.paginator import Paginator
from .models import Item
# Create your views here.


def index(request):
    items = Item.objects.all()

    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        items = items.filter(title__icontains=item_name)

    paginator = Paginator(items, 6)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    return render(request, 'index.html', {'items': items})


def detail(request, id):
    item = Item.objects.get(id=id)
    return render(request, 'details.html', {'item': item})


def cart_view(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


