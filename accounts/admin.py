from django.contrib import admin

from accounts.models import Profile, Position, Department, Company


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'company', 'position', 'department']


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['company', 'title']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['company', 'title', 'head']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['title', 'email']
