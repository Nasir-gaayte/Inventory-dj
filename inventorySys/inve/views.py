import inspect
from django.shortcuts import get_object_or_404, redirect, render 
from django.contrib.auth.decorators import login_required
from django.urls import is_valid_path
from .models import Inventory
from .forms import InventoryForm

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
    
@login_required
def update_inve(request,id):
    inve = get_object_or_404(Inventory,pk=id)
    form=InventoryForm(request.POST or None ,instance=inve)
    if form.is_valid():
        form.save()
        return redirect('index')    
            
    form = InventoryForm()
    return render(request,'inve/update.html',{
        'form':form
    })   
    