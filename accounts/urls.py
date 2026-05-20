from django.urls import path
from .views import login_view, dashboard_view, logout_view, register

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),
]