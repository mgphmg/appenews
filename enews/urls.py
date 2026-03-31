from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('login-options/', views.login_options, name='login_options'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('user_home/', views.user_home, name='user_home'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('editor_home/', views.editor_home, name='editor_home'),
    path('reporter_home/', views.reporter_home, name='reporter_home'),
    path('logout/', views.user_logout, name='logout'),
    path('article/', views.admin_article, name='admin_article'),
]
