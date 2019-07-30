from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auth_app.urls'), name='login'),
    path('dashboard/', include('dashboard.urls'), name='dashboard')
]
