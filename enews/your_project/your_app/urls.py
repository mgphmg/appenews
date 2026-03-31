from django.urls import path
from . import views

urlpatterns = [
    path('user-login/', views.user_login, name='user_login'),
]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('your_app.urls')),
]