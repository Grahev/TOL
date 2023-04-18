from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import JsonResponse
from .models import Project, ProjectNotes, Status, ProjectStatusHistory
from .serializers import ProjectSerializer
from rest_framework.decorators import api_view
from .forms import ProjectForm, ProjectNotesForm
from .filters import ProjectFilter
from django.contrib import messages
from django.utils import timezone


# Create your views here.

def project_list(request):
    projects = ProjectFilter(request.GET, queryset=Project.objects.all())

    context = {'projects': projects}
    return render (request, 'project_list.html', context)

def project_detail(request,pk):
    project = Project.objects.get(pk=pk)

    # Define a dictionary that maps each status to a URL that updates the project status
    status_urls = {
        'Approved': reverse('tracker:update_project_status', args=[project.pk, 'Approved']),
        'Waiting': reverse('tracker:update_project_status', args=[project.pk, 'Waiting on approval']),
        'Ordered': reverse('tracker:update_project_status', args=[project.pk, 'Ordered']),
        'Production': reverse('tracker:update_project_status', args=[project.pk, 'Production']),
        'Dispatch': reverse('tracker:update_project_status', args=[project.pk, 'Dispatch']),
    }

    context = {
        'project':project,
        'status_urls': status_urls,
    }
    return render (request, 'project_detail.html', context)

def update_project_status(request, pk, status):
    project = Project.objects.get(id=pk)
    project.status = Status.objects.get(name=status) 
    project.save()

    history = ProjectStatusHistory.objects.create(
        project=project,
        status=Status.objects.get(name=status),
        user = request.user,
        date_time=timezone.now(),
    )

    return redirect('tracker:project_detail', pk=project.pk)
    # return redirect(reverse('project_detail', args=[project_id]))

def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('tracker:project_detail', pk=project.pk)
    return render(request, 'project_form.html', {'form': form})

#project by engineer/user view witch are loged in
def project_by_engineer(request):
    user = request.user.username
    projects = ProjectFilter(request.GET, queryset=Project.objects.filter(project_engineer=user))

    context = {'projects': projects}
    return render(request, 'project_list.html', context)

#create note for specified job only- view
def create_note(request, pk):
    if request.method == "POST":
        form = ProjectNotesForm(request.POST)
        if form.is_valid():
            note_instance = form.save(commit=False)
            note_instance.project = Project.objects.get(pk=pk)
            note_instance.user = request.user
            note_instance.save()
            return redirect(reverse('tracker:project_detail', args=[pk]))
    else:
        form = ProjectNotesForm()

    return render(request,'create_note.html', {'form':form})

#delete note view
def delete_note(request, pk):
    note = get_object_or_404(ProjectNotes, pk=pk)
    if request.user == note.user:
        note.delete()
        return redirect('tracker:project_detail', pk=note.project.pk)
    else:
        messages.warning(request, "You don't have permission to delete this note.")
        return redirect('tracker:project_detail', pk=note.project.pk)
    
#API views
# @api_view('GET')
def project_list_api(request):
    project = Project.objects.all()
    serializer = ProjectSerializer(project, many=True)
    return JsonResponse({'projects': serializer.data}, safe=False)