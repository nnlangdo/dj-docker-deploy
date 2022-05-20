from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('viewpage/', views.viewpage, name='viewpage'),
    # path('saveform', views.saveform, name='saveform'),
    path('saveform/', views.AddDonationView.as_view(), name='saveform'),
    path('editreceipt/<int:pk>/',views.EditReceiptView.as_view(),name='editreceipt'),

    path('receipt-bg/', views.receipt_bg, name='receipt-bg'),
    path('receipt-main/', views.receipt_main, name='receipt-main'),
    path('receipt-download/<int:id>/', views.receipt_download, name='receipt-download'),
]
