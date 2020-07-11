from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroups.as_view(), name='all'),
    path('new/', views.CreateGroup.as_view(), name='create'),
    # this might cause Problems...
    path('posts/in/<slug>/', views.SingleGroup.as_view(), name='single'),
]
