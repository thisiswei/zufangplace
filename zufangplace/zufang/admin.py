from django.contrib import admin

from . import models


class UserProfileAdmin(admin.ModelAdmin):
    pass


class FangAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'is_studio',
        'num_bedroom',
        'num_bathroom',
        'date_avaialable',
    )

    class Meta:
        ordering = (
            '-date_avaialable',
        )


class AddressAdmin(admin.ModelAdmin):
    pass



admin.site.register(models.UserProfile, UserProfileAdmin)
admin.site.register(models.Fang, FangAdmin)
admin.site.register(models.Address, AddressAdmin)
