from django import forms
from .models import Product, Category, Event, Medida
from django.core.exceptions import ValidationError
from ckeditor.widgets import CKEditorWidget

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'categoria_id', 'evento_id', 'medida_id', 'image' ]
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Producto'}),
            'description': CKEditorWidget(),
            'price': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Price'}),
            'categoria_id': forms.Select(attrs={'class':'form-control'}),
            'evento_id': forms.Select(attrs={'class':'form-control'}),
            'medida_id': forms.Select(attrs={'class':'form-control'}),
        }

        labels = {
            'title': "",
            'description': ""
        }
        
class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Categoría'}),
            
        }

        labels = {
            'name': "",
            
        }

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['name','image' ]
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Evento'}),
            'description': CKEditorWidget(),
        }

        labels = {
            'name': "",
            'description': ""
        }
        
class MedidaForm(forms.ModelForm):

    class Meta:
        model = Medida
        fields = ['name' , 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Medida'}),
            'description': CKEditorWidget(),
        }

        labels = {
            'name': "",
            'description': ""
        }

