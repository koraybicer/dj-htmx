from django.urls import path
from components.todo.todo import TodoComponent
from . import views

urlpatterns = [
    path("components/todo", TodoComponent.as_view(), name="todos"),
    path("components/todo/<int:pk>/", TodoComponent.as_view(), name="todo"),
    path('', views.index, name='index'),

]
