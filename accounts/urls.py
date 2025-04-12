from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('api/user-info/', views.UserInfoAPIView.as_view(), name='user-info'),
]