from django.contrib import admin
from .models import User


# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email')


admin.site.register(User, RegisterAdmin)
