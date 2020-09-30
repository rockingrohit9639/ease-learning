"""DigiLibs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="Hompage"),
    path('resources', views.resources, name="Resources"),
    path('getresources/<str:sem>', views.get_resources, name="Get Resources"),
    path('add_requirements', views.add_requirements, name="Add Requirements"),
    path('about', views.about, name="About Us"),
    path('feedback', views.feedback, name="Feedback"),
    path('logout', views.handle_logout, name="LogOut"),
    path('login', views.hande_login, name="Login"),
    path('signup', views.handle_signup, name="SignUp"),
    path('search', views.search, name="Search"),
    path('blog', views.blog, name="Blog"),
    path('blog/<slug:slug>', views.post, name="Blog Post"),
    path('add_post', views.add_post, name="Add New Blog Post View"),
    path('add_new_post', views.add_new_post, name="Add New Post"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
