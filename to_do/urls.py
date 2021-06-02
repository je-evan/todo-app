from django.urls import path
from to_do import views

urlpatterns = [
    path('add/', views.TodoCreateView.as_view(), name = 'add'),
    path('list/', views.TodoListView.as_view(), name = 'list'),
    path('detail/<int:pk>', views.TodoDetailView.as_view(), name = 'detail'),
    path('update/<int:pk>', views.TodoUpdateView.as_view(), name = 'update'),
    path('delete/<int:pk>', views.TodoDeleteView.as_view(), name = 'delete'),
]