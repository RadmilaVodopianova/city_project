from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('sport/', include('sport.urls')),
    path('cars/', include('cars.urls')),
    path('weekdays/', include('weekdays.urls')),

    path('', include('city.urls')),
]