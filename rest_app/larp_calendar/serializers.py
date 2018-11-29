from rest_framework import serializers

from larp_calendar import models


class LarpSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Larp
        fields = (
            'name', 'organizer', 'website', 'image',
            'date_start', 'date_end', 'description', 'validated',
        )
        read_only_fields = ('validated',)
