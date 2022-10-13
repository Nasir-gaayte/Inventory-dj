from re import M
from unicodedata import decimal
from django.db import models



class Inventory(models.Model):
    name = models.CharField(max_length= 100, null= False, blank=False)
    cost_product = models.DecimalField(max_digits = 20, decimal_places = 2, null=False, blank=False)
    qty_in_stock = models.IntegerField(null=False, blank=False)
    qty_sold = models.IntegerField(null=False, blank=False)
    sales = models.DecimalField(max_digits = 20, decimal_places = 2, null=False, blank=False)
    stack_date = models.DateField(auto_now_add=True)
    last_sales_date = models.DateField(auto_now=True)
    
    
    def __str__(self):
        return self.name



# name  cost_product  qty_in_stock  qty_sold sales  stack_date last_sales_date 