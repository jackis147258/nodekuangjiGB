"""
URL configuration for moon39 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from app1 import views
from tcAdmin.admin import tcAdmin_site   
from rest_framework.documentation import include_docs_urls
from django.urls import re_path
from django.contrib.staticfiles.views import serve
from django.views.generic.base import RedirectView



# def return_static(request, path, insecure=True, **kwargs):
#   return serve(request, path, insecure, **kwargs)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tcadmin/', tcAdmin_site.urls),
    path('', RedirectView.as_view(url='/admin/'), name='redirect-to-admin'),

    # path('',  admin.site.urls),
    # path('', include('app1.urls')),
    path('app1/', include('app1.urls')),  
    path('apiv1/', include('apiV1.urls')),  
    path('reg/', include('reg.urls')),  

    # path("docs/", include_docs_urls(title="DRF API文档", description="Django REST framework快速入门")),
    path('websocket/', views.websocket_view, name='websocket'),    
   
    # re_path(r'^static/(?P<path>.*)$', return_static, name='static'), # 添加这行
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#         urlpatterns += [re_path(r'^static/(?P<path>.*)$', return_static, name='static')]
 