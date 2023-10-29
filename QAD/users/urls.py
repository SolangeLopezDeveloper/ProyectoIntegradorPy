from django.urls import path
from .views import HomeView, SignUpView, AboutView, ProfileView, ProfileEditView, CartView, OrdersView, MyLoginView, LogoutView

urlpatterns = [
    path('home/', HomeView.as_view(), name="home"),
    path('about/', AboutView.as_view(), name="about"),

    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileEditView.as_view(), name='edit_profile'),
    
    path('cart/', CartView.as_view(), name='cart'),
    path('orders/', OrdersView.as_view(), name='orders'),
    
    path('login/',  MyLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),

]