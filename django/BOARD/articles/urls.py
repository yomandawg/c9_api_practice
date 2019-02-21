from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"), # name: alias
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('<int:article_id>/', views.detail, name="detail"),
    path('<int:article_id>/edit/', views.edit, name="edit"),
    path('<int:article_id>/update/', views.update, name="update"),
    path('<int:article_id>/delete/', views.delete, name="delete"),
    path('<int:article_id>/comment/', views.comment, name="comment"),
]