from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  *

router = DefaultRouter()
router.register(r'building', BuildingViewSet)
router.register(r'elevator', ElevatorViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('delete-all-data/', delete_all_data, name='delete-all-data'),
    path('start_lift/', start_lift, name='start_lift'),
    path('liftStatus/', liftStatus, name='liftStatus'),

]
