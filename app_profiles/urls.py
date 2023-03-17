from django.urls import path

from app_profiles.views import RegisterView, PersonalAccount, TopUp, BuyProduct, AuthView

urlpatterns = [
    path('register/', RegisterView, name='register'),
    path('personal_account/', PersonalAccount, name='personal_account'),
    path('top_up/', TopUp, name='top_up'),
    path('buy_product/<int:shop_id>/<int:product_id>/', BuyProduct, name='buy_product'),
    path('auth/', AuthView, name='auth_page')
]