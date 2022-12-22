from django.urls import path
from accounts.views import login_view, logout_view, RegisterView
app_name = 'accounts'


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('register/', register_view, name='register'),
]
