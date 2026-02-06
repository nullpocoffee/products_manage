from django.db import models

# Create your models here.
from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=255, verbose_name="メーカー名")
    street_address = models.CharField(max_length=255, verbose_name="住所")
    representative_name = models.CharField(max_length=255, verbose_name="代表者名")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name

class Product(models.Model):
    # blank=True, null=True を追加して、画像なしを許可します
    img_path = models.ImageField(upload_to='products/', verbose_name="商品画像", blank=True, null=True)
    product_name = models.CharField(max_length=255, verbose_name="商品名")
    price = models.IntegerField(verbose_name="価格")
    # default=0 を追加して、未入力でも0になるようにします
    stocks = models.PositiveIntegerField(verbose_name="在庫数", default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="メーカー")
    comment = models.TextField(blank=True, null=True, verbose_name="コメント")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name