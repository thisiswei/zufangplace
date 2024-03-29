from django.contrib import admin

from . import models


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone',
    )

    def name(self, obj):
        return obj.user.username


class FangAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'is_studio',
        'num_bedroom',
        'num_bathroom',
        'date_available',
        'city',
        'state',
        'price_rent',
        'price_buy',
    )

    class Meta:
        ordering = (
            '-date_available',
        )


class PictureAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.UserProfile, UserProfileAdmin)
admin.site.register(models.Fang, FangAdmin)
admin.site.register(models.Picture, PictureAdmin)
