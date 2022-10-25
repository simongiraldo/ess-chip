from django.contrib import admin
from users.models import Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    
    list_display = ('pk', 'user', 'email', 'saldo', 'bloqueado', 'carrera')
    list_editable = ('saldo', 'bloqueado')

    fieldsets = (
        ('Profile', {
            'fields': ('user', 'email', 'carrera'),
        }),
        ('Carnet', {
            'fields': ('saldo', 'bloqueado')
        })
    )

class ProfileInline(admin.StackedInline):

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):

    inlines = (ProfileInline,)
    list_display = ('pk', 'username', 'email', 'is_active', 'is_staff')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)