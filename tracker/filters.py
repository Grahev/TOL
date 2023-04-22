import django_filters
from tracker.models import Project

class ProjectFilter(django_filters.FilterSet):
    
    class Meta:
        model = Project
        fields = ['job_no','customer','project_engineer','status']