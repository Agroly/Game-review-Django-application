from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='user-register'),
    path('login/', views.LoginView.as_view(), name='user-login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('profile/', views.ProfileUpdateView.as_view(), name='user-profile'),
    path('admin/<int:pk>/role/', views.RoleUpdateView.as_view(), name='admin-role-update'),
]
