"""
URL configuration for taskmanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from rest_framework import routers
from tasks.views import TaskViewSet
from django.http import HttpResponse
from rest_framework.authtoken.views import obtain_auth_token

#home view
def home(request):
    return HttpResponse("Welcome to Task Manager API")

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)



urlpatterns = [
     path('', home),  #home route
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),  # for login in browsable API
    path('api/', include('tasks.urls')), 
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
