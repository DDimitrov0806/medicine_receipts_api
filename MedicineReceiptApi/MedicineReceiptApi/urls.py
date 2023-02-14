from django.contrib import admin
from django.urls import path
from django.conf.urls import include
#from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    #path('auth/login/', obtain_jwt_token),
    #path('token/refresh-token/', TokenObtainPairView, name='token_obtain_pair'),
    #path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/', include('receipts.urls')),
]
