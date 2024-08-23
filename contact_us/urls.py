from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
# Router
router = DefaultRouter()

# antena
router.register('contact_us', views.ContactusViewset)
urlpatterns = [
    path('', include(router.urls)),
]
