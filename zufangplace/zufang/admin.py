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


class LikeAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'fang_id',
    )

    def username(self, obj):
        return obj.likinguser.user.username

    def fang_id(self, obj):
        return self.fang.id


admin.site.register(models.UserProfile, UserProfileAdmin)
admin.site.register(models.Fang, FangAdmin)
admin.site.register(models.Picture, PictureAdmin)
admin.site.register(models.Like, LikeAdmin)
