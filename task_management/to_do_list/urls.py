from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'task', views.UserTaskViewSet)

urlpatterns = [
    # path('tasks/', views.UserTaskViewSet.as_view({'get': 'list'})),
    # path('task/create/', views.UserTaskViewSet.as_view({'get': 'create'})),
    path('', include(router.urls)),
    # path('task/<int:pk>/', views.UserTaskViewSet.as_view({'get': 'retrieve'}))
]