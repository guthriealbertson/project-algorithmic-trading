from django.urls import path

from . import views

urlpatterns = [
    path('get_stock_data/<str:_stock_symbol>/', views.get_stock_data, name='get_stock_data'),
    path('get_stock_data_candle/<str:_stock_symbol>/', views.get_stock_data_candle, name='get_stock_data_candle'),
    path('save_investment/', views.SaveInvestment.as_view(), name='save_investment'),
    path('purchase_stock/', views.PurchaseStock.as_view(), name ='purchase_stock'),
    path('sell_stock/', views.SellStock.as_view(), name='sell_stock'),
    path('display_portfolio/', views.DisplayPortfolio.as_view(), name ='display_portfolio'),
    path('update_stocks_daily/', views.update_stocks_daily, name='update_stocks_daily'),
    path('delete_user_account/', views.DeleteAccount.as_view(), name='delete_user_account'),
]
