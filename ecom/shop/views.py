from django.shortcuts import render
from django.template.defaultfilters import title
from django.core.paginator import Paginator
from .models import Item, Order
import json

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

    if request.method == 'POST':
        items_json = request.POST.get('items', "")
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        city = request.POST.get('city', "")
        zipcode = request.POST.get('zipcode', "")

        # Check if items_json is being received correctly
        if items_json:
            print("Items received:", items_json)  # Debugging line

            # Create an Order instance
            order = Order(
                name=name,
                email=email,
                address=address,
                city=city,
                zipcode=zipcode,
                items=items_json,  # Directly save the JSON data
            )
            order.save()

    return render(request, 'checkout.html')


