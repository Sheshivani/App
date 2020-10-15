from django.contrib import admin
from .models import Register


# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','contact','email')


admin.site.register(Register,RegisterAdmin)
