from django.urls import path
from . import views
from django.contrib import admin
app_name = "notes"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:note_id>/', views.detail, name="detail")
    
]
