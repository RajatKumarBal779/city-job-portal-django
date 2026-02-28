"""
URL configuration for jobsproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from testapp import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page_view),
    path('jobs/<str:city>/',views.jobs_view,name='jobs_view'),
]

# <str:city> → dynamic part, Django captures whatever is in that position and passes it as a string to your view.
# name is a label or identifier for this URL pattern.