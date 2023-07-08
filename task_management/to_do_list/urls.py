from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'task', views.TaskViewSet)

urlpatterns = [
    path('my_tasks/', views.UserTask.as_view()),
    # path('task/create/', views.UserTaskViewSet.as_view({'get': 'create'})),
    path('', include(router.urls)),
    # path('task/<int:pk>/', views.UserTaskViewSet.as_view({'get': 'retrieve'}))
]