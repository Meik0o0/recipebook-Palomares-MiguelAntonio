from django.contrib import admin
from django.urls import include, path
from .views import index

urlpatterns = [
    path ('recipes/list/', views.recipe_list, name='recipe_list'),
    path('recipe/1/', views.recipe_1, name='recipe 1'),
    path('recipe/2/', views.recipe_2, name='recipe 2'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
]

app_name = "ledger"
