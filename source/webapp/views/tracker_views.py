from django.shortcuts import render, get_object_or_404, redirect, reverse
from webapp.models import Tracker
from django.views.generic import TemplateView, FormView, ListView
from webapp.forms import TackerForm, SimpleSearchForm
from webapp.base_validator import FormView as HandMadeFormView, ListView as HandMadeListView
from django.db.models import Q
from django.utils.http import urlencode

# Create your views here.

# class IndexView(HandMadeListView):
#     template_name = 'index.html'
#     context_key = 'trackers'
#
#     def get_objects(self):
#         return Tracker.objects.all().order_by('-created_at')


class IndexView(ListView):
    template_name = 'tracker/index.html'
    context_object_name = 'trackers'
    model = Tracker
    ordering = ('-created_at')
    paginate_by = 10

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


class InfoView(TemplateView):
    template_name = 'tracker/info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tracker'] = get_object_or_404(Tracker, pk=kwargs['pk'])
        return context


class DeleteView(TemplateView):
    template_name = 'tracker/delete.html'

    def get(self, request, *args, **kwargs):
        tracker = get_object_or_404(Tracker, pk=kwargs['pk'])
        return render(request, 'tracker/delete.html', context={'tracker': tracker})

    def post(self, request, *args, **kwargs):
        tracker = get_object_or_404(Tracker, pk=kwargs['pk'])
        tracker.delete()
        return redirect('index')


class AddView(HandMadeFormView):
    template_name = 'add.html'
    form_class = TackerForm

    def form_valid(self, form):
        types = form.cleaned_data.pop('type')
        self.tracker = Tracker.objects.create(**form.cleaned_data)
        self.tracker.type.set(types)
        return super().form_valid(form)

    def get_redirect_url(self):
        return reverse('info', kwargs={'pk': self.tracker.pk})


class UpdatedView(FormView):
    template_name = 'tracker/update.html'
    form_class = TackerForm

    def dispatch(self, request, *args, **kwargs):
        self.tracker = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tracker'] = self.tracker
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.tracker
        return kwargs

    def form_valid(self, form):
        self.tracker = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('info', kwargs={'pk': self.tracker.pk})

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Tracker, pk=pk)
