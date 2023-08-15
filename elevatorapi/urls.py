from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  BuildingViewSet,ElevatorViewSet

router = DefaultRouter()
router.register(r'building', BuildingViewSet)
router.register(r'elevator', ElevatorViewSet)


urlpatterns = [
    path('', include(router.urls)),
]