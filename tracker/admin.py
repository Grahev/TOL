from django.contrib import admin
from .models import Project, ProjectNotes, Status, ProjectStatusHistory

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('job_no', 'customer', 'order_value', 'status')
    list_filter = ('status', 'order_date', 'customer')
    search_fields = ('job_no', 'customer_order_ref', 'customer')

class ProjectNotesAdmin(admin.ModelAdmin):
    list_display = ('create_date', 'project', 'user')
    list_filter = ('create_date', 'project', 'user')
    search_fields = ('create_date', 'project', 'user')

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectNotes, ProjectNotesAdmin)
admin.site.register(Status)
admin.site.register(ProjectStatusHistory)
