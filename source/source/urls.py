"""source URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import IndexView, InfoView, AddView, UpdatedView, DeleteView
from webapp.views.project_views import ProjectIndexView, ProjectTrackerView, ProjectAddView, ProjectView, \
    ProjectDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProjectIndexView.as_view(), name='project_index'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_info'),
    path('project/list/trackers/', ProjectTrackerView.as_view(), name='project_tracker_info'),
    path('project/add/', ProjectAddView.as_view(), name='project_add'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),

    path('project/<int:pk>/add/tracker', AddView.as_view(), name='add'),

    path('tracker/list', IndexView.as_view(), name='index'),
    path('tracker/<int:pk>/', InfoView.as_view(), name='info'),
    path('tracker/<int:pk>/update/', UpdatedView.as_view(), name='update'),
    path('tracker/<int:pk>/delete/', DeleteView.as_view(), name='delete'),

]
