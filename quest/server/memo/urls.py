from django.urls import path
from . import views

app_name = 'memo'

urlpatterns = [
    path('memos/create/', views.memo_create),
    path('memos/', views.memo_list),
]