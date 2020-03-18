from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'ingredients_list/', views.ingredients_list),
    url(r'ingredients_detail/', views.ingredients_detail),
    url(r'ingredients_update_form/', views.ingredients_update_form),
    url(r'ingredients_create_form/', views.ingredients_create_form),

    url(r'recipes_list/', views.recipes_list),
    url(r'recipes_detail/', views.recipes_detail),
    url(r'recipes_update_form/', views.recipes_update_form),
    url(r'recipes_create_form/', views.recipes_create_form),

    url(r'orders_list/', views.orders_list),
    url(r'orders_detail/', views.orders_detail),
    url(r'orders_update_form/', views.orders_update_form),
    url(r'orders_create_form/', views.orders_create_form),
]