from django.urls import path 
from .views.doctorView import DoctorView
from .views.medicineViews import MedicineView
from .views.pharmacyView import PharmacyView
 
urlpatterns = [ 
    path('medicine', MedicineView.as_view()),
    path('medicine/<int:id>', MedicineView.as_view()),
    path('doctor', DoctorView.as_view()),
    path('doctor/<int:id>', DoctorView.as_view()),
    path('pharmacy', PharmacyView.as_view()),
    path('pharmacy/<int:id>', PharmacyView.as_view())
]