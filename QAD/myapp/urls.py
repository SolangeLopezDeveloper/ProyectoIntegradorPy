from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('home/', HomeView.as_view(), name="home"),
    path('search/', BusquedaView.as_view(), name='search'),  
    
    path('productos/', ProductList.as_view(), name="productos"),
    path('productos_crear/', ProductCreate.as_view(), name="productos-crear"),
    path('productos_actualizar/<int:pk>/', ProductUpdate.as_view(), name="productos-actualizar"),
    path('productos_eliminar/<int:pk>/', ProductDelete.as_view(), name="productos-eliminar"),
    path('producto_detalle/<int:pk>/', ProductDetailView.as_view(), name="producto-detalle"),

    path('categorias/', CategoryList.as_view(), name="categorias"),
    path('categorias_crear/', CategoryCreate.as_view(), name="categorias-crear"),
    path('categorias_actualizar/<int:pk>/', CategoryUpdate.as_view(), name="categorias-actualizar"),
    path('categorias_eliminar/<int:pk>/', CategoryDelete.as_view(), name="categorias-eliminar"),

    path('eventos/', EventList.as_view(), name="eventos"),
    path('eventos_crear/', EventCreate.as_view(), name="eventos-crear"),
    path('eventos_actualizar/<int:pk>/', EventUpdate.as_view(), name="eventos-actualizar"),
    path('eventos_eliminar/<int:pk>/', EventDelete.as_view(), name="eventos-eliminar"),

    path('medida/', MedidaList.as_view(), name="medida"),
    path('medida_crear/', MedidaCreate.as_view(), name="medida-crear"),
    path('medida_actualizar/<int:pk>/', MedidaUpdate.as_view(), name="medida-actualizar"),
    path('medida_eliminar/<int:pk>/', MedidaDelete.as_view(), name="medida-eliminar"),

]