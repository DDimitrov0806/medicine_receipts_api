from django.urls import path 
from receipts.views import Receipts
 
urlpatterns = [ 
    path('<str:request_id>', Receipts.as_view()),
]