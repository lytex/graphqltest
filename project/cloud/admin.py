from django.contrib import admin

# Register your models here.

from django.contrib import admin
from cloud.models import User, App


class UserAdmin(admin.ModelAdmin):
    pass


class AppAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(App, AppAdmin)
