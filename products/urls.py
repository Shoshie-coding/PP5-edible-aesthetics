from django.urls import path
from . import views
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('', views.all_products, name='products'),
    path('create', staff_member_required(views.ProductCreateView.as_view()), name="create"),
    path('delete', views.delete, name='delete'),
    path('edit/<pk>', staff_member_required(views.ProductUpdateView.as_view()), name="edit"), 
    path('<product_id>', views.product_detail, name='product_detail'),
]
