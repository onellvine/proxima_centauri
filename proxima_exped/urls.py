from django.urls import path
from proxima_user import views as user_views
from . import views


urlpatterns = [
    path('', user_views.home, name='home'),
    path('<int:expedition_id>/', views.detail, name='detail'),
]