from multiprocessing import context
import django
from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render 
from django.contrib.auth.decorators import login_required
from .models import Inventory
from .forms import InventoryForm, UpdateInventoryForm
from django.views.generic import UpdateView
from django.urls import reverse
from django_pandas.io import read_frame
import plotly
import plotly_express as px
import json

# Create your views here.

@login_required
def index(request):
    inventorys = Inventory.objects.all()
    return render(request,'inve/index.html',{
        "inventorys":inventorys
    })
    
@login_required    
def veiw_detail(request, id):
    inve = get_object_or_404(Inventory,pk=id)
    return render(request,'inve/view_detail.html',{'inve':inve})
        
        
        
@login_required
def add_inventory(request):
    if request.method == "POST":
        form=InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')    
            
    form = InventoryForm()
    return render(request,'inve/add_inventory.html',{
        'form':form
    })        
    
# @login_required
# def update_inve(request,pk):
#     in_data = get_object_or_404 ( Inventory ,id=int(pk))
#     if request.method == "POSt":   
#         form=UpdateInventoryForm(data=request.POST)
#         if form.is_valid():
#             in_data.name = form.data['name'] 
#             in_data.cost_product= form.data['cost_product']
#             in_data.qty_in_stock = form.data['qty_in_stock']
#             in_data.qty_sold = form.data['qty_sold']
#             in_data.sales = float(in_data.cost_product)*float(in_data.qty_sold)
#             in_data.save()
#             return redirect('index')    
          
#     form = UpdateInventoryForm(instance=in_data)
#     return render(request,'inve/update.html',{
#         'form':form,
#     })   

class Updat_v(generic.UpdateView):
    model = Inventory
    form_class= InventoryForm
    template_name= 'inve/update.html'
    
@login_required    
def delete_v (request, id):
    invetory = get_object_or_404(Inventory, pk=id)   
    form = invetory
    if request.method == "POST":
        invetory.delete()
        return redirect('index')
    return render(request,'inve/delete.html',{'form':form})

# name  cost_product  qty_in_stock  qty_sold sales  stack_date last_sales_date 

# @login_required
# def dashboard(request):
#     inventores = Inventory.objects.all()  
   
    
#     df = read_frame(inventores)
    
#     sales_graph = df.groupby(by='last_sales_date', as_index=True, sort=False)["sales"]
#     sales_graph = px.line( y= sales_graph.sales)
#     sales_graph = px.line(x= sales_graph.last_sales_date)
#     sales_graph = px.line(title='SalesKN' )
#     sales_graph = json.dump(sales_graph, cls=plotly.utils.PlotlyJSONEncoder)
    
    
    
#     return render (request,'inve/dashboard.html',{'sales_graph':sales_graph})