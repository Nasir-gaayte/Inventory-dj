from django import forms
from .models import Inventory



class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ('__all__')
        
        

class UpdateInventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ( "name",  "cost_product",  "qty_in_stock",  "qty_sold")