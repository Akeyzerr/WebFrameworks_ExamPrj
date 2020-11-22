from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from PyWEB_Exam2 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
