from django import forms
from .models import Project, ProjectNotes



class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        # fields = ['job_no', 'comments']
        exclude = ['date_sent_for_approval', 'date_approval_recived', 'date_into_production','date_dispatch','notes']

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['date_sent_for_approval', 'date_approval_recived', 'date_into_production','date_dispatch','notes','project_engineer','status']
        widgets = {
            'order_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'process_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'order_req_by_date': forms.widgets.DateInput(attrs={'type': 'date'}),
        }

class ProjectNotesForm(forms.ModelForm):
    class Meta:
        model = ProjectNotes
        fields = ('text',)


