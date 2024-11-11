from django.urls import path

from recipes.views import RecipeList

from .views import search_google

urlpatterns = [
    path('recipes/', RecipeList.as_view(), name='recipe-list'),
    path('search-google/<str:search_term>/', search_google, ),
]
