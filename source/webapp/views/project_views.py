from django.shortcuts import reverse, get_object_or_404, redirect
from django.urls import reverse_lazy
from webapp.models import Project
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from webapp.forms import ProjectForm, SimpleSearchForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.utils.http import urlencode


class ProjectIndexView(ListView):
    template_name = 'project/index.html'
    context_object_name = 'projects'
    model = Project
    paginate_by = 3

    def get_queryset(self):
        soft_deletion = Project.objects.filter(is_deleted=False)
        return soft_deletion

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        if self.form.is_valid():
            self.search_value = self.form.cleaned_data['search']
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.search_value:
            queryset = Project.objects.filter(is_deleted=False)
        if self.search_value:
            query = Q(title__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search'] = self.search_value
        return context


class ProjectView(DetailView):
    template_name = 'project/info.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = self.object
        projects_fk = projects.projects_fk.order_by('-created_at')
        context['projects_fk'] = projects_fk
        return context


class ProjectAddView(LoginRequiredMixin, CreateView):

    template_name = 'project/add.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('webapp:project_info', kwargs={'pk': self.object.pk})


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'project/update.html'
    form_class = ProjectForm
    context_key = 'project'

    def get_success_url(self):
        return reverse('webapp:project_info', kwargs={'pk': self.object.pk})


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'project/delete.html'
    success_url = reverse_lazy('project_index')

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs['pk'])
        project.is_deleted = True
        project.save()
        return redirect('webapp:project_index')


# class ProjectDeleteView(DeleteView):
#     template_name = 'project/delete.html'
#     model = Project
#     context_object_name = 'project'
#     success_url = reverse_lazy('project_index')



