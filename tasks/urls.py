
# tasks/urls.py
from rest_framework import routers
from django.urls import path, include
from .views import TaskViewSet


router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename="task")

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')


urlpatterns = [
    path('', include(router.urls)),
]
