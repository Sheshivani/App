from django.contrib import admin
from .models import profile, User,buy, sell, article

# Register your models here.
class UserAdmin(admin.ModelAdmin):
     list_display = ('email', 'username', 'phone')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','address')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

# class BuyAdmin(admin.ModelAdmin):
#      list_display = ({'article_name': 'name'})

admin.site.register(User, UserAdmin)
admin.site.register(profile, ProfileAdmin)
admin.site.register(article, ArticleAdmin)
admin.site.register(buy)
admin.site.register(sell)

