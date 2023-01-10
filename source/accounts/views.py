from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, reverse
from django.views.generic.list import MultipleObjectMixin
from accounts.forms import MyUserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView, DetailView, ListView
from .models import Profile


class RegisterView(CreateView):
    model = User
    template_name = 'user_create.html'
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('webapp:project_index')
        return next_url


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('webapp:project_index')
        else:
            context['has_error'] = True
    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('webapp:project_index')


class UserDetailView(LoginRequiredMixin, DetailView, MultipleObjectMixin):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    paginate_related_by = 3

    def get_context_data(self, **kwargs):
        project = self.get_object().user.all()
        return super().get_context_data(object_list=project, **kwargs)


class UsersList(PermissionRequiredMixin, ListView):
    model = get_user_model()
    template_name = 'user_list.html'
    context_object_name = 'user_obj'
    permission_required = 'accounts.can_see_users'

    def has_permission(self):
        return super().has_permission()