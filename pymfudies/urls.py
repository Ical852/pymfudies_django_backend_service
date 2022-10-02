from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import routers
from pymarket.viewsset_api import *

router = routers.DefaultRouter()
router.register('food', FoodViewSets)
router.register('notification', NotificationViewSets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    path('api/', include('pymarket.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)