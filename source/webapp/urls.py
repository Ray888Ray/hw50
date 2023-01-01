from django.urls import path
from webapp.views.tracker_views import IndexView, InfoView, AddView, UpdatedView, TrackerDeleteView
from webapp.views.project_views import ProjectIndexView, ProjectAddView, ProjectView, \
    ProjectDeleteView, ProjectUpdateView, AddUser, DeleteUser

app_name = 'webapp'

urlpatterns = [
    path('', ProjectIndexView.as_view(), name='project_index'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_info'),
    path('project/add/', ProjectAddView.as_view(), name='project_add'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('project/<int:pk>/add/tracker/', AddView.as_view(), name='add'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),

    path('tracker/list/', IndexView.as_view(), name='index'),
    path('tracker/<int:pk>/', InfoView.as_view(), name='info'),
    path('tracker/<int:pk>/update/', UpdatedView.as_view(), name='update'),
    path('tracker/<int:pk>/delete/', TrackerDeleteView.as_view(), name='delete'),

    path('user/<int:pk>/add', AddUser.as_view(), name='user_add'),
    path('user/<int:pk>/delete', DeleteUser.as_view(), name='user_delete'),

]
