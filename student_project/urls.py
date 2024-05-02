"""
URL configuration for student_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from studentapp.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/",AdminRegistrationView.as_view(),name="register"),
    path("login/",AdminLoginView.as_view(),name="login"),
    path('logins/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("department/",DepartmentAPIView.as_view(),name="department"),
    path("department/<int:pk>/",DepartmentAPIView.as_view(),name="department"),
    path("student/",StudProfileAPIView.as_view(),name="student"),
    path('student/<int:pk>/', StudProfileAPIView.as_view(), name='student-detail'),
]
