from django.urls import path 
from .views import MedicineView
 
urlpatterns = [ 
    path('', MedicineView.as_view()),
    path('<int:id>/', MedicineView.as_view())
]