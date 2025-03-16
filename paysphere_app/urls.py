from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    home, CustomLoginView, RegisterView, UserViewSet,ActivateUserView,DeactivateUserView
)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', home, name='home'),
    path('api/login/', CustomLoginView.as_view(), name='login'),
    # path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='register_user'),
    path('api/', include(router.urls)),
    path('user/activate/<int:user_id>/', ActivateUserView.as_view(), name='activate_user'),
    path('user/deactivate/<int:user_id>/',DeactivateUserView.as_view(), name='deactivate_user'),
]
