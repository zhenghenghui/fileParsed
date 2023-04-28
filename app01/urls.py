from django.contrib import admin
from django.urls import path,include
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('register/',views.register),
    path('getFile',views.getFile),
]