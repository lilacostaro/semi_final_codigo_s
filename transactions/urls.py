from django.urls import path
from . import views

urlpatterns = [
    path('deposit/', views.MakeDepositView.as_view(), name='make_deposit'),
    path('withdraw/', views.MakeWithdrawView.as_view(), name='make_withdraw'),
    path('transfer/', views.MakeTransferView.as_view(), name='make_transactions'),
    path('list_all_transactions/', views.ListAllTransactionsView.as_view(), name='list_all_transactions'),
    path('list_last_week_transactions/', views.ListLastWeekTransactionsView.as_view(), name='list_last_week_transactions'),
    path('list_last_month_transactions/', views.ListLastMonthTransactionsView.as_view(), name='list_last_month_transactions'),
    path('list_last_trimester_transactions/', views.ListLastTrimesterTransactionsView.as_view(), name='list_last_trimester_transactions')
]