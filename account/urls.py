from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(redirect_field_name='/cycles/'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register_user, name='register')
]
