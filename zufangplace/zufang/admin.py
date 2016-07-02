from django.contrib import admin

from . import models


class UserProfileAdmin(admin.ModelAdmin):
    pass

class FangAdmin(admin.ModelAdmin):
    class Meta:
        ordering = (
            '-date_avaialable',
        )

# Register your models here.

admin.site.register(models.UserProfile, UserProfileAdmin)
admin.site.register(models.Fang, FangAdmin)
