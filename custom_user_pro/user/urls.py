from django.urls import path
from . import views
urlpatterns = [
    path('', views.index_page, name='home-page'),
    path('login/', views.login_page, name='login-page'),
    path('logout/', views.logout_page, name='logout-page'),
    path('register/', views.register_page, name='register-page'),

    path('users/create/', views.user_create, name='user-create')
]