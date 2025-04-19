from django.urls import path
from .views import TodoListCreate, TodoRetrieveUpdateDestroy

urlpatterns = [
    path('', TodoListCreate.as_view()),
    path('<int:pk>/', TodoRetrieveUpdateDestroy.as_view()),
]