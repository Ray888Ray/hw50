from django.shortcuts import reverse, get_object_or_404, render, redirect
from django.urls import reverse_lazy
from webapp.models import Project
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from webapp.forms import ProjectForm


class ProjectIndexView(ListView):
    template_name = 'project/index.html'
    context_object_name = 'projects'
    model = Project
    paginate_by = 3

    def get_queryset(self):
        soft_deletion = Project.objects.filter(is_deleted=False)
        return soft_deletion


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


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project/update.html'
    form_class = ProjectForm
    context_key = 'project'

    def get_success_url(self):
        return reverse('project_info', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    template_name = 'project/delete.html'
    success_url = reverse_lazy('project_index')

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs['pk'])
        project.is_deleted = True
        project.save()
        return redirect('project_index')


# class ProjectDeleteView(DeleteView):
#     template_name = 'project/delete.html'
#     model = Project
#     context_object_name = 'project'
#     success_url = reverse_lazy('project_index')



