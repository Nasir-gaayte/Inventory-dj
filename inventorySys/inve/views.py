
from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render 
from django.contrib.auth.decorators import login_required
from .models import Inventory
from .forms import InventoryForm
from django.views.generic import UpdateView
from django.urls import reverse


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
#     invetory = Inventory.objects.get(id=int(pk))
   
#     print(invetory)
#     form=InventoryForm(request.POST or None ,instance=invetory)
#     if form.is_valid():
#         form.save()
#         return redirect('index')    
            
#     form = InventoryForm()
#     return render(request,'inve/update.html',{
#         'invetory':invetory,
#         'form':form,
#     })   

class Updat_v(generic.UpdateView):
    model = Inventory
    form_class= InventoryForm
    template_name= 'inve/update.html'
    
    
def delete_v (request, id):
    invetory = get_object_or_404(Inventory, pk=id)   
    form = invetory
    if request.method == "POST":
        invetory.delete()
        return redirect('index')
    return render(request,'inve/delete.html',{'form':form})
    
    
    
    