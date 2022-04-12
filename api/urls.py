from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView
)

urlpatterns = [
    path('token/',views.MyTokenObtainPairView.as_view(),name="token_obtain_view"),
    path('token/refresh', TokenRefreshView.as_view(),name="refresh_view"),
    path('register/',views.RegisterView.as_view(),name='auth'),
    path('notes/',views.getNotes, name="notes"),
    path('', views.getRoutes),
    
]
