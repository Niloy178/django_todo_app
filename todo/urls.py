from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('mark_done/<int:pk>/', views.mark_done, name="mark_done"),
    path('mark_undone/<int:pk>', views.mark_undone, name="mark_undone"),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('edit_task/<int:pk>', views.edit_task, name="edit_task")
]