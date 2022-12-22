from django.shortcuts import get_object_or_404, reverse
from django.urls import reverse_lazy
from webapp.models import Tracker, Project
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from webapp.forms import TackerForm, SimpleSearchForm
from django.db.models import Q
from django.utils.http import urlencode

# Create your views here.


class IndexView(ListView):
    template_name = 'tracker/index.html'
    context_object_name = 'trackers'
    model = Tracker
    ordering = '-created_at'
    paginate_by = 10

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
        if self.search_value:
            query = Q(short_description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search'] = self.search_value
        return context


class InfoView(DetailView):
    template_name = 'tracker/info.html'
    model = Tracker


class TrackerDeleteView(DeleteView):
    model = Tracker

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('webapp:project_index')


class AddView(CreateView):
    template_name = 'tracker/add.html'
    model = Tracker
    form_class = TackerForm

    def get_success_url(self):
        return reverse('webapp:project_info', kwargs={'pk': self.object.project_fk.pk})

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        form.instance.project_fk = project
        return super().form_valid(form)


class UpdatedView(UpdateView):
    model = Tracker
    template_name = 'tracker/update.html'
    form_class = TackerForm
    context_object_name = 'tracker'

    def get_success_url(self):
        return reverse('webapp:info', kwargs={'pk': self.object.pk})

