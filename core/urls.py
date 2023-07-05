from django.contrib import admin
from django.urls import path, include
from . import yasg

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.mainapp.urls')),
    path('api/v2', include('mailer_project.urls')),
]

urlpatterns += yasg.urlpatterns