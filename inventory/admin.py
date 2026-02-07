from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Company, Product

# 管理画面にモデルを登録
admin.site.register(Company)
admin.site.register(Product)