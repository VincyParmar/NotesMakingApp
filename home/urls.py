from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homeview.as_view(), name='home'),
    path('login/', views.LogninInterfaceView.as_view(), name='login'),
    path('logout/', views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup'),
]