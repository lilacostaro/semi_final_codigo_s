from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateAccountView.as_view(), name='create_account'),
    # path('<int:account_id>', views.AccountDetailView.as_view(), name='account_detail'),
]