from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('etl/', include('firestation_etl.urls')),
    path('admin/', admin.site.urls),
]