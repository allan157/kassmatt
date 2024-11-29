from django.shortcuts import render
from .models import Product

def store(request):
    products = Product.objects.all().filter(is_available=True)
    product_count = products.count()
    
    context = {
        'products' : products,
        'product_count': product_count,  # Added product count to the context for display in the template.  # Added product count to the context for display in the template.  # Added product count to the context for display in the template.  # Added product count to the context for display in the template.  # Added product count to the context for display in the template.  # Added product count to the context for display in the template.  # Added product count to
    }
    return render(request, 'store/store.html', context) 