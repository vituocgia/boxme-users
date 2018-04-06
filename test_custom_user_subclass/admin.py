from django.contrib import admin
from boxme_user.admin import BoxmeUserAdmin
from .models import MyCustomBoxmeUser


class MyCustomBoxmeUserAdmin(BoxmeUserAdmin):
    pass

# Register your models here.
admin.site.register(MyCustomBoxmeUser, MyCustomBoxmeUserAdmin)
