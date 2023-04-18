from django import forms
from .models import Project, ProjectNotes

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectNotesForm(forms.ModelForm):
    class Meta:
        model = ProjectNotes
        fields = ('text',)