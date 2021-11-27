
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('service.urls'), name='service_urls'),
    path('accounts/', include('allauth.urls')),
    path('service_booking/', include('service_booking.urls')),
]
