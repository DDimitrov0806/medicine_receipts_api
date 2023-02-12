from django.urls import path 
from receipts.views import MedicineView
 
urlpatterns = [ 
    path('medicines/', MedicineView.as_view()),
    path('medicines/<int:id>/', MedicineView.as_view())
]