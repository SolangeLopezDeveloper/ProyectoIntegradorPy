from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages


from .models import Product, Category, Event, Medida
from .forms import ProductForm, CategoryForm, EventForm, MedidaForm

from django.views.generic import TemplateView , DetailView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


from django.contrib.auth.views import LoginView

class HomeView(TemplateView):
    template_name = "users/home.html"

""" CRUD CATEGORÍAS """
class CategoryList(ListView):
    model = Category
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['titulo'] = "Lista de Categorias"
        return contexto

class CategoryCreate(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('categorias')
    
class CategoryUpdate(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name_suffix= "_update_form"
    
    def get_success_url(self):
        return reverse_lazy('categorias-actualizar', args=[self.object.id])+"?ok"
    
class CategoryDelete(DeleteView):
    model= Category
    success_url = reverse_lazy('categorias')



""" CRUD EVENTOS """   

class EventList(ListView):
    model = Event
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['titulo'] = "Lista de Eventos"
        return contexto

class EventCreate(CreateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('eventos')
    
class EventUpdate(UpdateView):
    model = Event
    form_class = EventForm
    template_name_suffix= "_update_form"
    
    def get_success_url(self):
        return reverse_lazy('eventos-actualizar', args=[self.object.id])+"?ok"
    
class EventDelete(DeleteView):
    model= Event
    success_url = reverse_lazy('eventos')



""" CRUD MEDIDAS """

class MedidaList(ListView):
    model = Medida
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['titulo'] = "Lista de Medidas"
        return contexto

class MedidaCreate(CreateView):
    model = Medida
    form_class = MedidaForm
    success_url = reverse_lazy('medida')
    
class MedidaUpdate(UpdateView):
    model = Medida
    form_class = MedidaForm
    template_name_suffix= "_update_form"
    
    def get_success_url(self):
        return reverse_lazy('medida-actualizar', args=[self.object.id])+"?ok"
    
class MedidaDelete(DeleteView):
    model= Medida
    success_url = reverse_lazy('medida')



""" CRUD PRODUCTOS """

class ProductList(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product
    template_name = 'myapp/product_detail.html' 
    context_object_name = 'producto'     
    
class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('productos')
    
def form_valid(self, form):
    categoria_id = form.cleaned_data['categoria_id']
    product = form.save(commit=False)
    product.categoria_id_id = categoria_id 
    product.save()
    return super(ProductCreate, self).form_valid(form)
    
class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name_suffix= "_update_form"
    
    def get_object(self, queryset=None):
        return Product.objects.get(pk=self.kwargs['pk'])
    
    def get_success_url(self):
        return reverse_lazy('productos-actualizar', args=[self.object.pk]) + "?ok"
    
class ProductDelete(DeleteView):
    model= Product
    success_url = reverse_lazy('productos')


class BusquedaView(ListView):
    model = Product
    template_name = 'myapp/search.html'
    context_object_name = 'resultados'

    def get_queryset(self):
        search_query = self.request.GET.get('q', '')  # Obtiene el valor del campo de búsqueda desde la URL
        if search_query:
            queryset = Product.objects.filter(title__icontains=search_query)  # Realiza la búsqueda en el campo 'title'
        else:
            queryset = Product.objects.all()  # Si no se proporciona una consulta, muestra todos los productos
        return queryset