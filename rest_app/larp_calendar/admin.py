from django.contrib import admin

from larp_calendar import models


class LarpAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Larp, LarpAdmin)
