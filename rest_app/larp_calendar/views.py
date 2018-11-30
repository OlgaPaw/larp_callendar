from rest_framework import viewsets

from larp_calendar.models import Larp as LarpModel
from larp_calendar.serializers import LarpSerializer


class LarpViewSet(viewsets.ModelViewSet):
    queryset = LarpModel.objects.filter(validated=True)
    serializer_class = LarpSerializer
    http_method_names = ['get', 'post', 'head', 'options']
