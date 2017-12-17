from django.urls import include,path
from django.contrib import admin

urlpatterns = [
    path('videogameshelf/', include('videogameshelf.urls')),
    path('admin/', admin.site.urls),
]
