from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('account/register',views.register,name='register'),
    path('account/login',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout/',LogoutView.as_view(),name='logout'),
]
