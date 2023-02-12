from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('easyleasy2.urls')),
    path('api/', include('api.urls')),
]
