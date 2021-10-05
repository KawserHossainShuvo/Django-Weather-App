from django.urls import path
from .views import cityweatherview, City_delete

app_name = 'app'

urlpatterns = [
    path('', cityweatherview, name="city"),
    path('remove/<city_name>/', City_delete, name="city_remove"),
]
