from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  *

router = DefaultRouter()
router.register(r'building', BuildingViewSet)
router.register(r'elevator', ElevatorViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('deleteAllData/', deleteAllData, name='deleteAllData'),
    path('requestLift/', requestLift, name='requestLift'),
    path('liftStatus/', liftStatus, name='liftStatus'),

]
