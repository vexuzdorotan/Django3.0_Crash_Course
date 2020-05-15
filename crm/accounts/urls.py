from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),

    path('', views.home, name='home'),
    path('user/', views.user_page, name='user'),

    path('account/', views.account, name='account'),

    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>', views.customer, name='customer'),

    path('create_order/<int:pk>', views.create_order, name='create_order'),
    path('update_order/<int:pk>', views.update_order, name='update_order'),
    path('delete_order/<int:pk>', views.delete_order, name='delete_order'),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name='accounts/password_reset.html'),
         name='password_reset'),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'), name='password_reset_confirm'),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_complete'),
]
