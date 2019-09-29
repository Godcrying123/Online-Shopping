from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('register/', views.RegistrationView.as_view()),
    path('profile/<int:pk>/', views.ProfileView.as_view()),
    path('profile/', views.ProfileView.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
