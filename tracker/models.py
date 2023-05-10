from django.db import models
# from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User, Group

# Create your models here.

class Status(models.Model):
    name = models.CharField(max_length=50)
    bootstrap_colour_class = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.name

class ProjectStatusHistory(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='status_history')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='project_history')
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.project} - {self.status} - {self.date_time}')

class Project(models.Model):
    job_no = models.CharField(max_length=10)
    job_type = models.CharField(max_length=25)
    customer_order_ref = models.CharField(max_length=55)
    order_date = models.DateField()
    process_date = models.DateField()
    order_value = models.IntegerField()
    customer = models.CharField(max_length=55)
    account_type = models.CharField(max_length=25)
    project_engineer = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True, limit_choices_to={'groups__name':'Project engineer'})
    # project_engineer = models.CharField(max_length=50, blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='projects', default=1)
    doors_s = models.IntegerField(default=0)
    doors_d = models.IntegerField(default=0)
    order_req_by_date = models.DateField(blank=True, null=True)
    handling_floor_plans =models.BooleanField(default=False)
    comments = models.CharField(max_length=1000, blank=True, null=True)
    date_sent_for_approval = models.DateField(max_length=25, null=True, blank=True)
    date_approval_recived = models.DateField(max_length=25, null=True, blank=True)
    date_into_production = models.DateField(max_length=25, null=True, blank=True)
    date_dispatch = models.DateField(max_length=25, null=True, blank=True)
    notes = models.ForeignKey('ProjectNotes', on_delete=models.CASCADE, related_name='project_notes', blank=True, null=True)

    def __str__(self):
        return (f'{self.job_no} - {self.customer}')
    
    @property
    def waiting(self):
        waiting = ProjectStatusHistory.objects.filter(
        project=self.pk,
        status = Status.objects.get(name='Waiting on approval')
        ).order_by('-date_time').first()
        return waiting
    
    @property
    def approved(self):
        approved = ProjectStatusHistory.objects.filter(
        project=self.pk,
        status = Status.objects.get(name='Approved')
        ).order_by('-date_time').first()
        return approved

    @property
    def production(self):
        production = ProjectStatusHistory.objects.filter(
        project=self.pk,
        status = Status.objects.get(name='Production')
        ).order_by('-date_time').first()
        return production

    @property
    def dispatch(self):
        dispatch = ProjectStatusHistory.objects.filter(
        project=self.pk,
        status = Status.objects.get(name='Dispatch')
        ).order_by('-date_time').first()
        return dispatch


class ProjectNotes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    create_date = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_notes')

    def __str__(self):
        return(f'{self.project} - {self.create_date}')
