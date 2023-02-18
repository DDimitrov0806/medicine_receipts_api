from django.urls import path

from receipts.views.loginView import LoginView
from receipts.views.registerView import RegisterView 
from .views.medicineViews import MedicineView
from .views.pharmacyView import PharmacyView
from .views.doctorView import DoctorView
from .views.patientView import PatientView
from .views.pharmacyMedicineView import PharmacyMedicineView
 
urlpatterns = [ 
    path('medicine', MedicineView.as_view()),
    path('medicine/<int:id>', MedicineView.as_view()),
    path('pharmacy', PharmacyView.as_view()),
    path('pharmacy/<int:id>', PharmacyView.as_view()),
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('patient', PatientView.as_view()),
    path('patient/<int:doctor_id>', PatientView.as_view()),
    path('doctor',DoctorView.as_view()),
    path('pharmacy-medicine', PharmacyMedicineView.as_view())
]