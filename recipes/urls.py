from django.urls import path
from recipes.views import home

#http request


urlpatterns = [
    path('', home), # home
    
]
