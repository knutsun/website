from api.viewsets import EventViewSet, SermonViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('events', EventViewSet)
router.register('sermons', SermonViewSet)
