from django.contrib import admin
from .models import ToDoUser,Organization,OrganizationJoinRequest
# Register your models here.

admin.site.register(ToDoUser)
admin.site.register(Organization)
admin.site.register(OrganizationJoinRequest)