"""
URL mappings for the recipe app
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()
router.register('recipes', views.RecipeViewSet) # This will create a new endpoint i.e 'recipes/' and it will assign all of the different endpoints from our RecipeViewSet
#It will create all of the different options for the viewset
#I.E. 'GET', 'POST', 'PUT', 'DELETE', 'PATCH'

app_name = 'recipe'  # It will be used to reverse() lookup of the vieset

urlpatterns = [
    path('', include(router.urls)),
]