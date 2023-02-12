from django.urls import path 
from receipts.views import ReceiptView
 
urlpatterns = [ 
    path('', ReceiptView.as_view()),
    path('<int:id>/', ReceiptView.as_view())
]