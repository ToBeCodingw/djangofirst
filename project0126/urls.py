"""
URL configuration for project0126 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
#include는 url의 처리를 다른 모듈에게 위임하고자 할 때 사용하는 패키지
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("example/", include("app0126.urls")),
    #위 문장은 example로 시작하는 요청이 오면 app0126 애플리케이션의 urls파일에 처리를 위임
]
