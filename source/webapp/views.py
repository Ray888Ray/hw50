from django.shortcuts import render, get_object_or_404, redirect, reverse
from webapp.models import Tracker
from django.views.generic import TemplateView
from webapp.forms import TackerForm
from django.views.generic import FormView
from .base_validator import FormView as HandMadeView


# Create your views here.

class IndexView(TemplateView):
   def get(self, request, *args, **kwargs):
       trackers = Tracker.objects.all()
       context = {
           'trackers': trackers
       }
       return render(request, 'index.html', context)


class InfoView(TemplateView):
   template_name = 'info.html'

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['tracker'] = get_object_or_404(Tracker, pk=kwargs['pk'])
       return context


class DeleteView(TemplateView):
    template_name = 'delete.html'

    def get(self, request, *args, **kwargs):
        tracker = get_object_or_404(Tracker, pk=kwargs['pk'])
        return render(request, 'delete.html', context={'tracker': tracker})

    def post(self, request, *args, **kwargs):
        tracker = get_object_or_404(Tracker, pk=kwargs['pk'])
        tracker.delete()
        return redirect('index')


class AddView(HandMadeView):
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
    template_name = 'update.html'
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