from django.contrib import admin
from  .models import WorkTypes
# Register your models here.

class WorkTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_deleted')
    # list_filter = ('is_deleted', 'role')
    # search_fields = ('name', 'role')

admin.site.register(WorkTypes, WorkTypeAdmin)
