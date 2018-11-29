from rest_framework import routers

from larp_calendar.views import LarpViewSet


router = routers.SimpleRouter()
router.register('larps', LarpViewSet)
