# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User, Profile
# Register your models here.

class CustomUserAdmin(UserAdmin):
    """ User model admin. """
    list_display = ('email','username','first_name','phone_number','is_staff','is_pollster', 'is_admin', 'is_verified')
    list_filter = ('is_admin','is_pollster', 'is_staff','created','modified')
    
    actions = ['is_pollster','is_not_pollster','is_admin','is_not_admin']

    def is_pollster(self, request, queryset):
        '''Make pollster is false'''
        queryset.update(is_pollster=False)
    is_pollster.short_description = 'Make selected user is not pollster'

    def is_not_pollster(self, request, queryset):
        '''Make pollster is true'''
        queryset.update(is_pollster=True)
    is_not_pollster.short_description = 'Make selected user is pollster'

    def is_admin(self, request, queryset):
        '''Make admin is false'''
        queryset.update(is_admin=True)
    is_admin.short_description = 'Make selected user is not admin'

    def is_not_admin(self, request, queryset):
        '''Make admin is true'''
        queryset.update(is_admin=False)
    is_admin.short_description = 'Make selected user is admin'

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Profile model admin ."""
    list_display = ('user','created','polls')
    search_fields = ('user_username','user__email','user__first_name','user__last_name')

admin.site.register(User, CustomUserAdmin)
