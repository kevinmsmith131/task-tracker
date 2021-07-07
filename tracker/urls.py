from django.urls import path
from .views import TaskList, TaskInfo, TaskCreate, TaskUpdate, TaskDelete, TaskToggle

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskInfo.as_view(), name='task'),
    path('task-create', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('task-toggle<int:pk>', TaskToggle.as_view(), name='task-toggle')
]