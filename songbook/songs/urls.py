from django.urls import path
from . import views

app_name = 'songs'

#endpoints
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('add/', views.SongCreate.as_view(), name='add_song')
]
