from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, DetailView, TemplateView, UpdateView
from .models import User, Cart, Order, Address
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class HomeView(TemplateView):
    template_name = "users/home.html"

class AboutView(TemplateView):
    template_name = "users/about.html"

""" LOGIN """  
  
class MyLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_invalid(self, form):
        messages.error(self.request, "Usuario o contraseña inválidos")
        return self.render_to_response(self.get_context_data(form=form))


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    
    def get_success_url(self):
        user_id = self.object.id
        return reverse('profile', args=[user_id])



class CartView(TemplateView):
    template_name = 'users/cart.html'

class OrdersView(TemplateView):
    template_name = 'users/orders.html'


class ProfileView(DetailView):
    model = User
    template_name = 'users/profile.html'   
    
class ProfileEditView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    fields = ['username', 'email']

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        user = self.request.user
        street = self.request.POST.get('street')
        city = self.request.POST.get('city')
        country = self.request.POST.get('country')

        address, created = Address.objects.get_or_create(user=user)
        address.street = street
        address.city = city
        address.country = country
        address.save()

        return redirect('profile')