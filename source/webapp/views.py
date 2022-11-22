from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Tracker, Status, Type
from django.views.generic import TemplateView
from webapp.forms import TackerForm


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


class AddView(TemplateView):
    template_name = 'add.html'

    def get(self, request, *args, **kwargs):
        form = TackerForm()
        return render(request, "add.html", {'form': form})

    def post(self, request, *args, **kwargs):
        form = TackerForm(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop('type')
            new_tracker = Tracker.objects.create( **form.cleaned_data)
            new_tracker.type.set(types)
            return redirect('info', pk=new_tracker.pk)
        else:
            return render(request, 'add.html', {'form': form})


class UpdatedView(TemplateView):
    template_name = 'update.html'

    def get(self, request, *args, **kwargs):
        tracker = get_object_or_404(Tracker, pk=kwargs['pk'])
        form = TackerForm(initial={
            'short_description': tracker.short_description,
            'content': tracker.content,
            'type': tracker.type.all(),
            'status': tracker.status})
        return render(request, 'update.html', {'form': form})

    def post(self, request, *args, **kwargs):
        tracker = get_object_or_404(Tracker, pk=kwargs['pk'])
        form = TackerForm(data=request.POST)
        if form.is_valid():
            tracker.short_description = form.cleaned_data.get('short_description')
            tracker.content = form.cleaned_data.get('content')
            tracker.status = form.cleaned_data.get('status')
            tracker.save()
            tracker.type.set(form.cleaned_data['type'])
            return redirect('info', pk=tracker.pk)
        else:
            return render(request, 'update.html', {'form': form})


class DeleteView(TemplateView):
    template_name = 'delete.html'

    def get(self, request, *args, **kwargs):
        tracker = get_object_or_404(Tracker, pk=kwargs['pk'])
        return render(request, 'delete.html', context={'tracker': tracker})

    def post(self, request, *args, **kwargs):
        tracker = get_object_or_404(Tracker, pk=kwargs['pk'])
        tracker.delete()
        return redirect('index')