"""
URL configuration for refund_system_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from refund_sytem.views import (
    index,
    SignUpView,
    RefundRequestListView,
    RefundRequestDetailView,
    CreateRefundRequestView,
    ValidateIBANView
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('refunds/', RefundRequestListView.as_view(), name='refund_list'),
    path('refunds/create/', CreateRefundRequestView.as_view(), name='create_refund'),
    path('refunds/<int:pk>/', RefundRequestDetailView.as_view(), name='refund_detail'),
    path('api/validate-iban/', ValidateIBANView.as_view(), name='validate_iban'),
]
