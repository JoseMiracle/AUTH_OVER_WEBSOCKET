from django.urls import path
from accounts.views import RegisterAPIView, LoginAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('log-in/', LoginAPIView.as_view(), name='login')
]


