from .views import TeamAPIView, TaskAPIView, UpdateTaskView, UserRegister, UpdateStatusView
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from taskapp import views


urlpatterns = [
    path('register/', UserRegister.as_view(), name="register"),
    path('team/', TeamAPIView.as_view(), name="team"),
    path('task/', TaskAPIView.as_view(), name="task"),
    path('task_update/<int:pk>/', UpdateTaskView.as_view(), name="update"),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('update_status/<int:pk>/', UpdateStatusView.as_view(), name='update_status'),
]
