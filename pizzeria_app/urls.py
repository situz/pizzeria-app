"""Defines URL patterns for pizzeria_app."""
from django.conf.urls import url
from . import views

app_name = 'pizzeria_app'
urlpatterns = [
    # Home Page
    url(r'^$', views.index, name='index'),
    # Show all pizzas
    url(r'^pizzas$', views.pizzas, name='pizzas'),
    # Detail page for a single pizza
    url(r'^pizzas/(?P<pizza_id>\d+)/$', views.pizza, name='pizza'),
    # Page for adding a new pizza
    url(r'^new_pizza/$', views.new_pizza, name='new_pizza'),
    # Page for adding a new topping
    url(r'^new_topping/(?P<pizza_id>\d+)/$', views.new_topping, name='new_topping'),
    # Page for editing a new topping
    url(r'^edit_topping/(?P<topping_id>\d+)/$', views.edit_topping, name='edit_topping'),
]
