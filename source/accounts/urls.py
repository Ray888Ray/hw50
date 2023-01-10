from django.urls import path
from accounts.views import login_view, logout_view, RegisterView, UserDetailView, UsersList
from django.conf import settings
from django.conf.urls.static import static
app_name = 'accounts'


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='profile'),
    path('users/', UsersList.as_view(), name='user_list' ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
