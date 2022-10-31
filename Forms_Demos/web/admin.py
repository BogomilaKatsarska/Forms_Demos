from django.contrib import admin

from Forms_Demos.web.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass
