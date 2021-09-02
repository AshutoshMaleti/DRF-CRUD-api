from django.urls import path
from base import views

urlpatterns = [
    path('',views.apiOverview,name='apiOverview'),
    path('task-list',views.taskList,name='taskList'),
    path('task-details/<str:pk>',views.detailedView,name='detailedView'),
    path('task-create',views.create,name='create'),
    path('task-update/<str:pk>',views.update,name='update'),
    path('task-delete/<str:pk>',views.delete,name='delete'),
]