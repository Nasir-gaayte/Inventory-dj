from django.urls import path
from inve import views
from .views import Updat_v


urlpatterns = [
    path('',views.index,name='index'),
    path('view_detail/<id>/',views.veiw_detail,name='view_detail'),
    path('add_inventory/',views.add_inventory,name='add_inventory'),
    # path('update/<int:pk>/',views.update_inve,name='update'),
    path('update/<int:pk>/',views.Updat_v.as_view(),name='update'),
    path('delete/<id>/',views.delete_v,name='delete'),
    # path('dashboard/',views.dashboard,name='dashboard'),
]
