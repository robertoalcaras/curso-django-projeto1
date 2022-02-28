from django.urls import path
from recipes.views import home, contato, sobre

#http request


urlpatterns = [
    path('', home), # home
    path('sobre/', sobre), # home
    path('contato/', contato), # home
]
