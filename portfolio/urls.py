from django.conf.urls import url
from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'portfolio'
urlpatterns = [

    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('stock_list', views.stock_list, name='stock_list'),
    path('stock/create/', views.stock_new, name='stock_new'),
    path('stock/<int:pk>/edit/', views.stock_edit, name='stock_edit'),
    path('stock/<int:pk>/delete/', views.stock_delete, name='stock_delete'),
    path('investment_list', views.investment_list, name='investment_list'),
    path('investment/create/', views.investment_new, name='investment_new'),
    path('investment/<int:pk>/edit/', views.investment_edit, name='investment_edit'),
    path('investment/<int:pk>/delete/', views.investment_delete, name='investment_delete'),
    path('customer/<int:pk>/portfolio/', views.portfolio, name='portfolio'),
    path('mutualfund_list', views.mutualfund_list, name='mutualfund_list'),
    path('mutualfund/create/', views.mutualfund_new, name='mutualfund_new'),
    path('mutualfund/<int:pk>/edit/', views.mutualfund_edit, name='mutualfund_edit'),
    path('mutualfund/<int:pk>/delete/', views.mutualfund_delete, name='mutualfund_delete'),
    url(r'^customers_json/', views.CustomerList.as_view()),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/success/$', views.register_success, name='success'),
]

urlpatterns = format_suffix_patterns(urlpatterns)