# # from django.urls import path
# # from rest_framework.routers import DefaultRouter
# # from .views import UserViewSet

# # router = DefaultRouter()
# # router.register(r'users', UserViewSet)

# # urlpatterns = router.urls



# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import UserViewSet, RegisterView

# router = DefaultRouter()
# router.register(r'users', UserViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('register/', RegisterView.as_view(), name='register'),
# ]



# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import RegisterView, UserViewSet, UserDetailView, UserUpdateView, UserDeleteView, ActivateDeactivateUserView,CustomAuthTokenView
# from rest_framework.authtoken.views import obtain_auth_token

# router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='user')

# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', CustomAuthTokenView.as_view(), name='login'),
    
#     path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
#     path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
#     path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
#     path('users/activate-deactivate/<int:pk>/', ActivateDeactivateUserView.as_view(), name='user-activate-deactivate'),
#     path('', include(router.urls)),
# ]

# urlpatterns += router.urls




# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import (
#     RegisterView, UserViewSet, UserDetailView, UserUpdateView, 
#     UserDeleteView, ActivateDeactivateUserView, CustomAuthTokenView
# )

# router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='user')

# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', CustomAuthTokenView.as_view(), name='login'),
    
#     path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
#     path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
#     path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
#     path('users/activate-deactivate/<int:pk>/', ActivateDeactivateUserView.as_view(), name='user-activate-deactivate'),
#     path('', include(router.urls)),
# ]


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
