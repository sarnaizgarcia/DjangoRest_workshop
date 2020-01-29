from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path('v1/cars/', include('cars.urls'))
]