from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('isval/', views.isval),
    path('cube/<int:number>', views.cube),
    path('ispal/<str:words>', views.ispal),
    path('image/', views.image),
    path('artii/', views.artii),
    path('new/', views.new),
    path('papago/', views.papago),
    path('result/', views.result),
]