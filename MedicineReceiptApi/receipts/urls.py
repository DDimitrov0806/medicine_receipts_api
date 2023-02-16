from django.urls import path

from receipts.views.loginView import LoginView
from receipts.views.registerView import RegisterView 
from .views.medicineViews import MedicineView
from .views.pharmacyView import PharmacyView
 
urlpatterns = [ 
    path('medicine', MedicineView.as_view()),
    path('medicine/<int:id>', MedicineView.as_view()),
    path('pharmacy', PharmacyView.as_view()),
    path('pharmacy/<int:id>', PharmacyView.as_view()),
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view())
]