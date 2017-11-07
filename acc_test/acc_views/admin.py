from django.contrib import admin
from .models import Users, Accounts

#class UserAdmin(admin.ModelAdmin):
 #   list_display = ('first_name',)

class FileAdmin(admin.ModelAdmin):
    list_display = ['fileLink']
    readonly_fields = ['fileLink']

admin.site.register(Users)
admin.site.register(Accounts)
# Register your models here.
