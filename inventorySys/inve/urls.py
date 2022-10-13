from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('view_detail/<id>/',views.veiw_detail,name='view_detail'),
    path('add_inventory/',views.add_inventory,name='add_inventory'),
    path('update/<id>/',views.update_inve,name='update'),
]
