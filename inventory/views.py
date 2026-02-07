from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product

def product_list(request):
    # すべての商品データを取得
    products = Product.objects.all()
    # テンプレート（HTML）にデータを渡して表示
    return render(request, 'inventory/product_list.html', {'products': products})