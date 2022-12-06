from django.shortcuts import render, get_object_or_404, redirect, reverse
from webapp.models import Project, Tracker
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from webapp.forms import ProjectForm


class ProjectIndexView(ListView):
    template_name = 'project/index.html'
    context_object_name = 'projects'
    model = Project
    paginate_by = 3


class ProjectTrackerView(ListView):
    template_name = 'tracker/index.html'
    context_object_name = 'trackers'
    model = Tracker


class ProjectView(DetailView):
    template_name = 'project/info.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = self.object
        projects_fk = projects.projects_fk.order_by('-created_at')
        context['projects_fk'] = projects_fk
        return context


class ProjectAddView(CreateView):

    template_name = 'project/add.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_info', kwargs={'pk': self.object.pk})


class ProjectDeleteView(TemplateView):
    template_name = 'project/delete.html'

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs['pk'])
        return render(request, 'project/delete.html', context={'project': project})

    def post(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs['pk'])
        project.delete()
        return redirect('project_index')
